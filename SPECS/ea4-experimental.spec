Name: ea4-experimental
Version: 0.1
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4600 for more details
%define release_prefix 7
Release: %{release_prefix}%{?dist}.cpanel
Summary: Access the EA4 experimental repository

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
%config %{_sysconfdir}/yum.repos.d/EA4-experimental.repo

%changelog
* Sat Oct 28 2017 Cory McIntire <cory@cpanel.net> - 0.1-7
- EA-6890: set the repo file as a config file
 
* Tue Oct 11 2016 Dan Muey <dan@cpanel.net> - 0.1-6
- EA-5244: Change package name to match github for clarity

* Mon Jun 20 2016 Dan Muey <dan@cpanel.net> - 0.1-5
- EA-4383: Update Release value to OBS-proof versioning

* Thu Oct 22 2015 Darren Mobley <darren@cpanel.net> - 0.1-3
- Finalized path for mirrorlist in .repo file

* Fri Oct 16 2015 Darren Mobley <darren@cpanel.net> - 0.1-2
- Renaming release packages due to conflicts in ea- namespace

* Mon Oct 12 2015 Darren Mobley <darren@cpanel.net> - 0.1-1
- Renamed package

* Fri Oct 02 2015 Darren Mobley <darren@cpanel.net> - 0.1-0
- Inital spec file and package creation
