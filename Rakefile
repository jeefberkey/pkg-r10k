$: << File.expand_path( '../lib/', __FILE__ )

require 'fileutils'
require 'find'
require 'rake/clean'
require 'rubygems'
require 'simp/rake'
require 'erb'

Simp::Rake::Pkg.new(File.dirname(__FILE__))

@rakefile_dir=File.dirname(__FILE__)

CLEAN.include 'dist'
CLEAN.include 'pkg'
Find.find( @rakefile_dir ) do |path|
  if File.directory? path
    CLEAN.include path if File.basename(path) == 'tmp'
  else
    Find.prune
  end
end

def get_gem_deps(gem)
  deps = {}
  raw_deps = `gem dependency #{gem} --pipe -R`
  raw_deps.split("\n").each do |d|
    dep, version = d.split('--version')
    next if dep =~ /(rake|rspec)/

    deps[dep.strip] = {
      version: Gem.latest_version_for(dep),
      url: Gem.latest_spec_for(dep).homepage,
      license: Gem.latest_spec_for(dep).licenses || Gem.latest_spec_for(dep).license || 'Apache-2.0'
    }
  end
  deps
end

task :gen_rpmspec do
  # require 'pry';binding.pry
  r10k_info = {
    version: `bundle show r10k`.split('-')[-1].strip,
    url: `gemdiff find r10k 2> /dev/null`.strip
  }
  r10k_deps = get_gem_deps('r10k')
  gem_info  = r10k_deps.merge('r10k' => r10k_info)
  changelog = File.read('CHANGELOG')

  f = File.open('build/simp-vendored-r10k.spec', 'w')
  f << ERB.new(File.read('build/simp-vendored-r10k.spec.erb'), nil, '-').result(binding)
  f.close
end

namespace :pkg do
  directory 'dist'

  desc 'build rubygem sub-packages'
  task :gem => ['dist'] do
    gem_dirs = Dir.glob('ext/gems/*')

    gem_dirs.each do |gem_dir|
      Dir.chdir gem_dir do
        Dir['*.gemspec'].each do |spec_file|
          cmd = %Q{bundle exec gem build "#{spec_file}" &> /dev/null}
          sh cmd
          FileUtils.mkdir_p 'dist'
          FileUtils.mv Dir.glob('*.gem'), File.join(@rakefile_dir, 'dist')
        end
      end
    end
  end

  Rake::Task[:rpm].prerequisites.unshift(:gem)
end
# vim: syntax=ruby
