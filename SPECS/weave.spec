## package settings
%define debug_package  %{nil}

Name:           weave
Version:        2.6.0
Release:        0%{?dist}
Summary:        Simple, resilient multi-host containers networking and more.

Group:          System Environment/Daemons
License:        Apache License, version 2.0
URL:            https://www.weave.works

Source0:        https://github.com/weaveworks/%{name}/releases/download/v%{version}/%{name}
Source2:        %{name}.service
Source3:        %{name}.sysconfig

BuildRequires:  systemd-units

Requires(pre):      shadow-utils
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
Weave Net creates a virtual network that connects Docker containers across
multiple hosts and enables their automatic discovery.
With Weave Net, portable microservices-based applications consisting of
multiple containers can run anywhere: on one host, multiple hosts or even
across cloud providers and data centers.

%prep

%build

%install
## main binary
%{__install} -p -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

## sytem files
%{__install} -p -D -m 0640 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -p -D -m 0640 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%pre

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root,-)
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
