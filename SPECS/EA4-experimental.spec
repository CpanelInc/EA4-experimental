Name: ea-experimental-release
Version: 0.1
Release: 1%{?dist}
Summary: Access the EA4-experimental repository

Group: Development/Tools
License: BSD 2-Clause
Vendor: cPanel, Inc.
Requires: yum

%description
This package puts in please the EA4-experimental.repo file needed to use the software related to EA4 from cPanel that is still in an experimental state.

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -m 644 %_sourcedir/EA4-experimental.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/EA4-experimental.repo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/EA4-experimental.repo

%changelog
* Mon Oct 12 2015 Darren Mobley <darren@cpanel.net> - 0.1-1
- Renamed package

* Fri Oct 02 2015 Darren Mobley <darren@cpanel.net> - 0.1-0
- Inital spec file and package creation
