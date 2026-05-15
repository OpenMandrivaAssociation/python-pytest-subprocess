%define module pytest-subprocess
%define oname pytest_subprocess
%bcond tests 1

Name:		python-pytest-subprocess
Version:	1.6.0
Release:	1
Summary:	A plugin to fake subprocess for pytest
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pytest-subprocess
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(anyio)
BuildRequires:	python%{pyver}dist(docutils)
BuildRequires:	python%{pyver}dist(pygments)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
%endif
%description
A plugin to fake subprocess for pytest

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

# We dont need to do upstream coverage checks
sed -Ei '/\bcoverage\b/d' setup.py

# https://github.com/aklajnert/pytest-subprocess/issues/146
sed -i '/error/d' pytest.ini

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
# not building docs, test not required
pytest -k "not test_documentation"
%endif

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}*.*-info
