Summary: Exporter
Name: date-exporter
Version: 1.0.0
Release: 1%{?dist}
License: MIT
#Source0: %{name}-%{version}.tar.gz
Group: fmizokos
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: ${_prefix}
Requires: java-11-openjdk

%define INSTALLDIR %{buildroot}/usr/local/bin
%define SERVICEDIR %{buildroot}/usr/lib/systemd/system/
%description
%prep
%build

%install
%{__mkdir_p} %{RPM_BUILD_ROOT}%{__unitdir}

#%{__rm} -rf %{INSTALLDIR} %{SERVICEDIR}
%{__mkdir_p} %{INSTALLDIR} %{SERVICEDIR}
#%{__cp} -R %{usr_src_dir}/app/build/libs/app.jar %{INSTALLDIR}
%{__cp} -R /app/app/build/libs/app.jar %{INSTALLDIR}
#%{__cp} -R %{usr_src_dir}/dateoutput.service %{SERVICEDIR}
%{__cp} -R /app/dateoutput.service %{SERVICEDIR}

%post
/bin/systemctl daemon-reload

%preun

%postun
if [ $1 -eq 0 ]; then
	/bin/systemctl daemon-reload
	/bin/systemctl reset-failed
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,users,-)
/usr/lib/systemd/system/dateoutput.service
%defattr(755,root,users,-)
/usr/local/bin/app.jar
