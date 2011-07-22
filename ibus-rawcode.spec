Summary:	The Rawcode engine for IBus input platform
Name:		ibus-rawcode
Version:	1.3.1.20100707
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://fedorahosted.org/releases/i/b/ibus-rawcode/%{name}-%{version}.tar.gz
# Source0-md5:	7c7a5444d4e39c1870533aaf3b46e72c
Patch0:		%{name}-build.patch
URL:		https://fedorahosted.org/ibus-rawcode/
BuildRequires:	ibus-devel
BuildRequires:	pkgconfig
Requires:	ibus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Rawcode engine for IBus platform.

%prep
%setup -q
%patch0 -p1

%build
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
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-rawcode
%{_datadir}/ibus-rawcode
%{_datadir}/ibus/component/rawcode.xml
