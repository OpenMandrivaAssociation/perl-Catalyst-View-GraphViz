%define realname   Catalyst-View-GraphViz
%define version    0.05
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    GraphViz View Class
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::Plugin::SubRequest)
BuildRequires: perl(GraphViz)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
This is the Catalyst view class for the GraphViz manpage. Your application
subclass should inherit from this class.

This plugin renders the GraphViz object specified in
'$c->stash->{graphviz}->{graph}' into the '$c->stash->{graphviz}->{format}'
(one of e.g. png gif, or one of the other as_* methods described in the the
GraphViz manpage module. PNG is the default format.

The output is stored in '$c->response->output'.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

