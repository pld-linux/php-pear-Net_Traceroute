%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Traceroute
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Execute traceroute
Summary(pl):	%{_pearname} - uruchamianie programu traceroute
Name:		php-pear-%{_pearname}
Version:	0.21
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65d8a974d1285bc6844243b941046350
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OS independent wrapper class for executing traceroute calls.

This class has in PEAR status: %{_status}.

%description -l pl
Niezale¿na od systemu klasa, bêd±ca wrapperem do uruchamiania programu
traceroute.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs
%{php_pear_dir}/%{_class}/*.php
