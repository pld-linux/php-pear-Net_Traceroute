%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Traceroute
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - execute traceroute
Summary(pl.UTF-8):	%{_pearname} - uruchamianie programu traceroute
Name:		php-pear-%{_pearname}
Version:	0.21
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65d8a974d1285bc6844243b941046350
URL:		http://pear.php.net/package/Net_Traceroute/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OS independent wrapper class for executing traceroute calls.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Niezależna od systemu klasa, będąca wrapperem do uruchamiania programu
traceroute.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
