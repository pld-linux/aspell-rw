Summary:	Kinyarwanda dictionary for aspell
Summary(pl):	S³ownik rwandyjski dla aspella
Name:		aspell-rw
Version:	0.50
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/rw/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	d369916c4f4159b04e43daf31dde60c9
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kinyarwanda dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik rwandyjski (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
