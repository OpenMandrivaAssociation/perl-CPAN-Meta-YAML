%define upstream_name    CPAN-Meta-YAML
%define upstream_version 0.005

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Read and write a subset of YAML for CPAN Meta files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(vars)
BuildArch: noarch

%description
This module implements a subset of the YAML specification for use in
reading and writing CPAN metadata files like _META.yml_ and _MYMETA.yml_.
It should not be used for any other general YAML parsing or generation
task.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


