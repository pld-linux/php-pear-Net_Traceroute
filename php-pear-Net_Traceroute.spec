%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Traceroute
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Execute traceroute
Summary(pl):	%{_pearname} - Uruchamia program traceroute
Name:		php-pear-%{_pearname}
Version:	0.11
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	aa59db4a0a01ddb10a28c6cacaf37ff9
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OS independent wrapper class for executing traceroute calls.

This class has in PEAR status: %{_status}.

%description -l pl
Niezale�na od systemu klasa, b�d�ca wrapperem do uruchamiania programu
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
%{php_pear_dir}/%{_class}/*.php
