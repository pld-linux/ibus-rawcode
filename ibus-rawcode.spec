Summary:	The Rawcode engine for IBus input platform
Summary(pl.UTF-8):	Silnik Rawcode dla platformy wprowadzania IBus
Name:		ibus-rawcode
Version:	1.3.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://fedorahosted.org/releases/i/b/ibus-rawcode/%{name}-%{version}.tar.gz
# Source0-md5:	d6b758c092cd70ec2f2c937be77d87cf
URL:		https://fedorahosted.org/ibus-rawcode/
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	ibus-devel >= 1.2.99
BuildRequires:	pkgconfig
Requires:	ibus >= 1.2.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus Rawcode is rawcode ime engine for IBus, one can input unicode
character by just entering in hex value.

%description -l pl.UTF-8
IBus Rawcode to silnik IBus oparty na surowych kodach, pozwalający na
wprowadzanie znaków unikodowych poprzez wpisanie ich szesnastkowego
kodu.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# only single, empty locale (zh_CN) exists (as of 1.3.1)
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/ibus-engine-rawcode
%{_datadir}/ibus-rawcode
%{_datadir}/ibus/component/rawcode.xml
