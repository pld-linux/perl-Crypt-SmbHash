#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SmbHash
Summary:	Crypt::SmbHash Perl module - generate LM/NT hashes like smbpasswd
Summary(pl):	Modu� Perla Crypt::SmbHash - generuj�cy skr�ty LM/NT takie jak smbpasswd
Name:		perl-Crypt-SmbHash
Version:	0.02
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions to generate LM/NT hashes used in
Samba's 'password' files, like smbpasswd.

%description -l pl
Ten modu� udost�pnia funkcje do generowania skr�t�w LM/NT, u�ywanych
w plikach z has�ami dla Samby - tak, jak robi to program smbpasswd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/SmbHash.pm
%{_mandir}/man3/*