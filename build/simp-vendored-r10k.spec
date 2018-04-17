%global pkgname simp-r10k

%global gemdir /usr/share/simp/ruby
%global simp_bindir /usr/share/simp/bin
%global geminstdir %{gemdir}/%{pkgname}-%{version}

%global r10k_version 2.6.2

# gem2ruby's method of installing gems into mocked build roots will blow up
# unless this line is present:
%define _unpackaged_files_terminate_build 0

Summary: r10k with puppet-safe gem installation
Name: simp-vendored-r10k
Version: %{r10k_version}
Release: 0
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
Source0: %{name}-%{version}-%{release}.tar.gz
Requires: puppet-agent
Requires: %{name}-doc
Requires: rubygem(%{pkgname}-r10k) >= %{r10k_version}
Requires: rubygem(%{pkgname}-colored) >= 1.2
Requires: rubygem(%{pkgname}-cri) >= 2.6
Requires: rubygem(%{pkgname}-gettext-setup) >= 0.5
Requires: rubygem(%{pkgname}-log4r) >= 1.1
Requires: rubygem(%{pkgname}-minitar) >= 0.6
Requires: rubygem(%{pkgname}-multi_json) >= 1.1
Requires: rubygem(%{pkgname}-puppet_forge) >= 2.2
Requires: rubygem(%{pkgname}-rspec) >= 3.1
Requires: rubygem(%{pkgname}-yard) >= 0.9
BuildArch: noarch

%description
A vendored version of r10k designed to prevent conflicts with any other gems on
the system.

You do *not* need to use this package to install r10k. The traditional methods
documented on the Internet, or the version that ships with Puppet Enterprise
will also work.

This was specifically designed for situations where Internet access is
difficult or unattainable.

Binaries from this package will be located at %{simp_binpath} and will not be
in your path by default.

%package doc
Summary: Documentation for the SIMP r10k installation
Version: %{r10k_version}
Release: 0
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
BuildArch: noarch

%description doc

Documentation for the SIMP r10k installation including sample configuration and
postrun scripts suited to a SIMP environment.

%package gem-colored
Summary: A colored Gem for use with %{name}
Version: 1.2
Release: 0
License: MIT
URL: 
Source11: colored-1.2.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-colored) = 1.2
%description gem-colored

Gem dependency for %{name}

%package gem-cri
Summary: A cri Gem for use with %{name}
Version: 2.6
Release: 0
License: MIT
URL: https://github.com/ddfreyne/cri
Source12: cri-2.6.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-cri) = 2.6
%description gem-cri

Gem dependency for %{name}

%package gem-gettext-setup
Summary: A gettext-setup Gem for use with %{name}
Version: 0.5
Release: 0
License: MIT
URL: https://github.com/puppetlabs/gettext-setup-gem
Source13: gettext-setup-0.5.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-gettext-setup) = 0.5
%description gem-gettext-setup

Gem dependency for %{name}

%package gem-log4r
Summary: A log4r Gem for use with %{name}
Version: 1.1
Release: 0
License: MIT
URL: https://github.com/colbygk/log4r
Source14: log4r-1.1.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-log4r) = 1.1
%description gem-log4r

Gem dependency for %{name}

%package gem-minitar
Summary: A minitar Gem for use with %{name}
Version: 0.6
Release: 0
License: MIT
URL: https://github.com/halostatue/minitar/
Source15: minitar-0.6.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-minitar) = 0.6
%description gem-minitar

Gem dependency for %{name}

%package gem-multi_json
Summary: A multi_json Gem for use with %{name}
Version: 1.1
Release: 0
License: MIT
URL: http://github.com/intridea/multi_json
Source16: multi_json-1.1.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-multi_json) = 1.1
%description gem-multi_json

Gem dependency for %{name}

%package gem-puppet_forge
Summary: A puppet_forge Gem for use with %{name}
Version: 2.2
Release: 0
License: MIT
URL: https://github.com/puppetlabs/forge-ruby
Source17: puppet_forge-2.2.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-puppet_forge) = 2.2
%description gem-puppet_forge

Gem dependency for %{name}

%package gem-rspec
Summary: A rspec Gem for use with %{name}
Version: 3.1
Release: 0
License: MIT
URL: https://github.com/rspec/rspec
Source18: rspec-3.1.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-rspec) = 3.1
%description gem-rspec

Gem dependency for %{name}

%package gem-yard
Summary: A yard Gem for use with %{name}
Version: 0.9
Release: 0
License: MIT
URL: https://github.com/lsegal/yard
Source19: yard-0.9.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-yard) = 0.9
%description gem-yard

Gem dependency for %{name}

%package gem-r10k
Summary: A r10k Gem for use with %{name}
Version: 2.6.2
Release: 0
License: MIT
URL: https://github.com/puppetlabs/r10k
Source20: r10k-2.6.2.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-r10k) = 2.6.2
%description gem-r10k

Gem dependency for %{name}



%prep
%setup -q

%build

%install
echo "======= %setup PWD: ${PWD}"
echo "======= %setup gemdir: %{gemdir}"

mkdir -p %{buildroot}/%{gemdir}
mkdir -p %{buildroot}/%{geminstdir}
mkdir -p %{buildroot}/%{simp_bindir}
mkdir -p %{buildroot}/%{_var}/simp/cache/r10k

%{lua:
  for i=11,21 do
    print("gem install --local --install-dir ")
    print(rpm.expand("%{buildroot}"))
    print("/")
    print(rpm.expand("%{geminstdir}"))
    print(" --force ")
    print(rpm.expand("%{SOURCE"..i.."}\n"))
  end
}

cat <<EOM > %{buildroot}%{simp_bindir}/r10k
#!/bin/bash

export PATH=/opt/puppetlabs/bin:/opt/puppetlabs/puppet/bin:\$PATH
export GEM_PATH=%{geminstdir}:\$GEM_PATH

%{geminstdir}/gems/r10k-%{r10k_version}/bin/r10k \$@
EOM

%files
%defattr(0644, root, root, 0755)
%attr(0755,-,-) %{simp_bindir}/r10k
%dir %attr(0750,-,-) %{_var}/simp/cache/r10k

%files doc
%doc docs/*


%files gem-colored
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/colored-1.2
%exclude %{geminstdir}/cache/colored-1.2.gem
%{geminstdir}/specifications/colored-1.2.gemspec

%files gem-cri
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/cri-2.6
%exclude %{geminstdir}/cache/cri-2.6.gem
%{geminstdir}/specifications/cri-2.6.gemspec

%files gem-gettext-setup
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/gettext-setup-0.5
%exclude %{geminstdir}/cache/gettext-setup-0.5.gem
%{geminstdir}/specifications/gettext-setup-0.5.gemspec

%files gem-log4r
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/log4r-1.1
%exclude %{geminstdir}/cache/log4r-1.1.gem
%{geminstdir}/specifications/log4r-1.1.gemspec

%files gem-minitar
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/minitar-0.6
%exclude %{geminstdir}/cache/minitar-0.6.gem
%{geminstdir}/specifications/minitar-0.6.gemspec

%files gem-multi_json
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/multi_json-1.1
%exclude %{geminstdir}/cache/multi_json-1.1.gem
%{geminstdir}/specifications/multi_json-1.1.gemspec

%files gem-puppet_forge
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/puppet_forge-2.2
%exclude %{geminstdir}/cache/puppet_forge-2.2.gem
%{geminstdir}/specifications/puppet_forge-2.2.gemspec

%files gem-rspec
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/rspec-3.1
%exclude %{geminstdir}/cache/rspec-3.1.gem
%{geminstdir}/specifications/rspec-3.1.gemspec

%files gem-yard
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/yard-0.9
%exclude %{geminstdir}/cache/yard-0.9.gem
%{geminstdir}/specifications/yard-0.9.gemspec

%files gem-r10k
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/r10k-2.6.2
%exclude %{geminstdir}/cache/r10k-2.6.2.gem
%{geminstdir}/specifications/r10k-2.6.2.gemspec


%changelog
* Fri Sep 01 2017 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.2.2
- First release of r10k wrapper
