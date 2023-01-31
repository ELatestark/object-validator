%{!?__python3: %global __python3 /usr/bin/python3}

%global project_name object-validator
%global project_description %{expand:
This module is intended for validation of Python objects. For this time it's
supposed to be used for validation of configuration files represented as JSON
or for validation of JSON-PRC requests, but it can be easily extended to
validate arbitrary Python objects or to support custom validation rules.}

%bcond_without tests

Name:    python-%project_name
Version: 0.2.0
Release: 4.CROC2%{?dist}
Summary: Python object validation module

Group:   Development/Libraries
License: MIT
URL:     https://github.com/KonishchevDmitry/%project_name
Source:  http://pypi.python.org/packages/source/o/%project_name/%project_name-%version.tar.gz

BuildArch:     noarch
BuildRequires: make

%description %{project_description}


%package -n python%{python3_pkgversion}-%project_name
Summary: %{summary}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
%if 0%{with tests}
BuildRequires: python%{python3_pkgversion}-pytest >= 2.2.4
%endif  # with tests
Obsoletes: python36-%project_name
Conflicts: python36-%project_name

%description -n python%{python3_pkgversion}-%project_name %{project_description}


%prep
%setup -n %project_name-%version -q


%build
%py3_build


%check
make PYTHON=%{__python3} check

%install
%py3_install

%files -n python%{python3_pkgversion}-%project_name
%defattr(-,root,root,-)
%{python3_sitelib}/object_validator.py
%{python3_sitelib}/__pycache__/object_validator.*.py*
%{python3_sitelib}/object_validator-%{version}-*.egg-info
%doc ChangeLog README INSTALL

%clean
[ "%buildroot" = "/" ] || rm -rf "%buildroot"


%changelog
* Tue Jan 23 2023 Andrey Kulaev <adkulaev@gmail.com> - 0.2.0-4
- Add centos 8.4 support

* Sun Feb 10 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.2.0-3
- Enable tests for python36

* Wed Jan 09 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.2.0-2
- Add python3 package build for EPEL

* Thu Jan 11 2018 Dmitry Konishchev <konishchev@gmail.com> - 0.2.0-1
- Base class for number types with min/max validators
- flake8 linting and tox tests automation

* Tue Apr 26 2016 Dmitry Konishchev <konishchev@gmail.com> - 0.1.6-1
- Bump version because of PyPI error

* Tue Apr 26 2016 Dmitry Konishchev <konishchev@gmail.com> - 0.1.5-1
- min_length and max_length options for List validator

* Thu Sep 03 2015 Dmitry Konishchev <konishchev@gmail.com> - 0.1.4-1
- regex option for String validator

* Wed Feb 25 2015 Dmitry Konishchev <konishchev@gmail.com> - 0.1.3-1
- min_length and max_length options for String validator

* Tue Dec 16 2014 Dmitry Konishchev <konishchev@gmail.com> - 0.1.2-1
- delete_unknown parameter for DictScheme validator

* Mon Nov 24 2014 Dmitry Konishchev <konishchev@gmail.com> - 0.1.1-1
- New version.

* Fri Jul 05 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.1-1
- New package.
