%define module pytest-subprocess
%define oname pytest_subprocess
%bcond_without test

Name:		python-pytest-subprocess
Version:	1.5.3
Release:	2
Summary:	A plugin to fake subprocess for pytest
URL:		https://pypi.org/project/pytest-subprocess/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-subprocess/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
BuildRequires:	python%{pyver}dist(pygments)
BuildRequires:	python%{pyver}dist(docutils)
BuildRequires:	python%{pyver}dist(anyio)
%endif
%description
A plugin to fake subprocess for pytest

%prep
%autosetup -n %{oname}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

# https://github.com/aklajnert/pytest-subprocess/issues/146
sed -i '/error/d' pytest.ini

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
# not building docs, test not required
%{__python} -m pytest --import-mode append -v -k "not test_documentation"
%endif

%files
%{python3_sitelib}/%{oname}
%{python3_sitelib}/%{oname}-%{version}*.*-info
%license LICENSE
%doc README.rst
