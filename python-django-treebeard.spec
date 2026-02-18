%define module django-treebeard
%define oname django_treebeard

Name:		python-django-treebeard
Version:	5.0.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Efficient tree implementations for Django
URL:		https://pypi.org/project/django-treebeard/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{name} is a library that implements efficient tree
implementations for the Django Web Framework.

%prep
%autosetup -n %{oname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc README.md
%license LICENSE
%{python_sitelib}/treebeard
%{python_sitelib}/%{oname}-%{version}.dist-info
