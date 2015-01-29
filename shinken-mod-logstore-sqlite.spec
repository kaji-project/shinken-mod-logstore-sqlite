Name:		shinken-mod-logstore-sqlite
Version:	1.4.1
Release:	2kaji0.2
Summary:	Shinken Submodule Logstore Sqlite for Livestatus (Broker)

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/shinken-mod-logstore-sqlite
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

Requires:	shinken-mod-livestatus >= 1.0

%description
Shinken Logstore Sqlite submodule for Livestatus (Broker)

%prep
%setup -q


%build


%install
rm -rf %{buildroot}/*

install -d %{buildroot}/usr/share/pyshared/shinken/modules/logstore-sqlite
install -pm07555 module/* %{buildroot}/usr/share/pyshared/shinken/modules/logstore-sqlite 

install -d %{buildroot}/usr/share/doc/%{name}
install -pm0755 README.md %{buildroot}/%{_docdir}/%{name}

install -d %{buildroot}/etc/shinken/modules
install -pm0755 etc/modules/* %{buildroot}/etc/shinken/modules


%files
/usr/share/pyshared/shinken/modules/logstore-sqlite
%config(noreplace) %{_sysconfdir}/shinken/modules/

%doc %{_docdir}/%{name}


%changelog
* Thu Jan 22 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 1.4.1-2kaji0.2
- Initial Package
