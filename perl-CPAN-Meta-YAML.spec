%define	modname	CPAN-Meta-YAML
%define	modver	0.008

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Read and write a subset of YAML for CPAN Meta files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
BuildArch:	noarch

%description
This module implements a subset of the YAML specification for use in
reading and writing CPAN metadata files like _META.yml_ and _MYMETA.yml_.
It should not be used for any other general YAML parsing or generation
task.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.8.0-1
- cleanups
- new version

* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.5.0-1
+ Revision: 759439
- version update 0.005

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.3.0-2
+ Revision: 656884
- rebuild for updated spec-helper

* Mon Jan 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-1
+ Revision: 634486
- import perl-CPAN-Meta-YAML

