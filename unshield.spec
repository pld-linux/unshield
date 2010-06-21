Summary:	Program to extract CAB files
Summary(pl.UTF-8):	Program do rozpakowywania plików CAB
Name:		unshield
Version:	0.6
Release:	1
License:	MIT
Group:		Applications
Source0:	http://downloads.sourceforge.net/synce/Unshield/0.6/%{name}-%{version}.tar.gz
# Source0-md5:	31a829192a255160d1f71cda4c865c9c
URL:		http://www.synce.org/moin/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unshield extracts CAB files from an InstallShield installer archive.

%description -l pl.UTF-8
Unshield rozpakowuje pliki CAB z archiwum instalatora InstallShield.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/unshield
%attr(755,root,root) %{_libdir}/libunshield.so.*.*.*
%attr(755,root,root) %{_libdir}/libunshield.so.0
%{_mandir}/man1/unshield.1*
