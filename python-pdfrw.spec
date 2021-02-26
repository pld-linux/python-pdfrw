#
# Conditional build:
%bcond_with	tests	# unit tests (data missing in release tarball?)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	PDF file reader/writer library
Summary(pl.UTF-8):	Biblioteka do odczytu/zapisu plików PDF
Name:		python-pdfrw
Version:	0.4
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pdfrw/
Source0:	https://files.pythonhosted.org/packages/source/p/pdfrw/pdfrw-%{version}.tar.gz
# Source0-md5:	eaf97243d3634cac954527904dcdecae
URL:		https://pypi.org/project/pdfrw/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pdfrw is a Python library and utility that reads and writes PDF files:
- Operations include subsetting, merging, rotating, modifying metadata
- The fastest pure Python PDF parser available
- Has been used for years by a printer in pre-press production
- Can be used with rst2pdf to faithfully reproduce vector images
- Can be used either standalone, or in conjunction with reportlab
  to reuse existing PDFs in new ones
- Permissively licensed

%description -l pl.UTF-8
pdfrw to biblioteka i narzędzia Pythona do odczytu i zapisu plików
PDF:
- operacje obejmują wyciąganie fragmentów, łączenie, obracanie,
  modyfikowanie metadanych
- najszybszy dostępny czysto pythonowy parser formatu PDF
- używane latami w procesie przygotowywania do druku
- mogą być używane z rst2pdf do wiernej reprodukcji obrazów
  wektorowych
- mogą być używane samodzielnie lub w połączeniu z reportlabem do
  wykorzystywania istniejących plików PDF do tworzenia nowych
- wydane na nierestrykcyjnej licencji

%package -n python3-pdfrw
Summary:	PDF file reader/writer library
Summary(pl.UTF-8):	Biblioteka do odczytu/zapisu plików PDF
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pdfrw
pdfrw is a Python library and utility that reads and writes PDF files:
- Operations include subsetting, merging, rotating, modifying metadata
- The fastest pure Python PDF parser available
- Has been used for years by a printer in pre-press production
- Can be used with rst2pdf to faithfully reproduce vector images
- Can be used either standalone, or in conjunction with reportlab
  to reuse existing PDFs in new ones
- Permissively licensed

%description -n python3-pdfrw -l pl.UTF-8
pdfrw to biblioteka i narzędzia Pythona do odczytu i zapisu plików
PDF:
- operacje obejmują wyciąganie fragmentów, łączenie, obracanie,
  modyfikowanie metadanych
- najszybszy dostępny czysto pythonowy parser formatu PDF
- używane latami w procesie przygotowywania do druku
- mogą być używane z rst2pdf do wiernej reprodukcji obrazów
  wektorowych
- mogą być używane samodzielnie lub w połączeniu z reportlabem do
  wykorzystywania istniejących plików PDF do tworzenia nowych
- wydane na nierestrykcyjnej licencji

%prep
%setup -q -n pdfrw-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/python-pdfrw-%{version}
%{__sed} -i -e '1s,/usr/bin/env python$,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/python-pdfrw-%{version}{,/rl[12]}/*.py
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/python3-pdfrw-%{version}
%{__sed} -i -e '1s,/usr/bin/env python$,%{__python3},' $RPM_BUILD_ROOT%{_examplesdir}/python3-pdfrw-%{version}{,/rl[12]}/*.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/pdfrw
%{py_sitescriptdir}/pdfrw-%{version}-py*.egg-info
%{_examplesdir}/python-pdfrw-%{version}
%endif

%if %{with python3}
%files -n python3-pdfrw
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/pdfrw
%{py3_sitescriptdir}/pdfrw-%{version}-py*.egg-info
%{_examplesdir}/python3-pdfrw-%{version}
%endif
