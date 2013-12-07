%define	modname	CPAN-Meta-YAML
%define	modver	0.008

Summary:	Read and write a subset of YAML for CPAN Meta files
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)

%description
This module implements a subset of the YAML specification for use in
reading and writing CPAN metadata files like _META.yml_ and _MYMETA.yml_.
It should not be used for any other general YAML parsing or generation
task.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*

