#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SmbHash
Summary:	Crypt::SmbHash Perl module - generate LM/NT hashes like smbpasswd
Summary(pl.UTF-8):	Moduł Perla Crypt::SmbHash - generowanie skrótów LM/NT, takich jakie generuje smbpasswd
Name:		perl-Crypt-SmbHash
Version:	0.12
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a6e3f4d65a89bfcc9ba0c69691e6105b
URL:		http://search.cpan.org/dist/Crypt-SmbHash/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions to generate LM/NT hashes used in
Samba's 'password' files, like smbpasswd.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do generowania skrótów LM/NT, używanych
w plikach z hasłami dla Samby - tak, jak robi to program smbpasswd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
