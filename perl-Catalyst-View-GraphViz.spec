%define upstream_name    Catalyst-View-GraphViz
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	GraphViz View Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::Plugin::SubRequest)
BuildRequires:	perl(GraphViz)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This is the Catalyst view class for the GraphViz manpage. Your application
subclass should inherit from this class.

This plugin renders the GraphViz object specified in
'$c->stash->{graphviz}->{graph}' into the '$c->stash->{graphviz}->{format}'
(one of e.g. png gif, or one of the other as_* methods described in the the
GraphViz manpage module. PNG is the default format.

The output is stored in '$c->response->output'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

