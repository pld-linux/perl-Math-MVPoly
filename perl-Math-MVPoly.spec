#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	MVPoly
Summary:	MVPoly - multi-variable polynomial algebra library
Summary(pl):	MVPoly - biblioteka algebry na wielomianach z wieloma zmiennymi
Name:		perl-Math-MVPoly
Version:	0.8b
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	00d092600150b18848ea5b534c8cd334
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MVPoly is a multi-variable polynomial algebra library and command
interpreter. It implements the core algebraic functionality to support
operations upto and including determining Groebner Basis. Four
monomial orderings are supported: grlex, grevlex, lex, and total
degree. Variable orderings are also supported. A parser is included as
a means to construct a simple command-line interfaces similar to that
of Maple.

%description -l pl
MVPoly to biblioteka i interpreter algebry na wielomianach z wieloma
zmiennymi. Ma zaimplementowan± podstawow± funkcjonalno¶æ algebraiczn±,
aby obs³ugiwaæ operacje w³±cznie z okre¶laniem bazy Groebnera.
Obs³ugiwane s± cztery porz±dki jednomianów: grlex, grevlex, lex i
³±cznego stopnia.

%prep
%setup -q -n %{pnam}

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
%doc README
%{perl_vendorlib}/Math/MVPoly
%{_mandir}/man3/*
