#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-qtconsole
Version  : 5.3.2
Release  : 78
URL      : https://files.pythonhosted.org/packages/b5/cf/8916ee5bf560f54050e1beb195df2c048bf9f0f9fae171dc1aa09b09c0bd/qtconsole-5.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/cf/8916ee5bf560f54050e1beb195df2c048bf9f0f9fae171dc1aa09b09c0bd/qtconsole-5.3.2.tar.gz
Summary  : Jupyter Qt console
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-qtconsole-bin = %{version}-%{release}
Requires: pypi-qtconsole-license = %{version}-%{release}
Requires: pypi-qtconsole-python = %{version}-%{release}
Requires: pypi-qtconsole-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ipykernel)
BuildRequires : pypi(ipython_genutils)
BuildRequires : pypi(jupyter_client)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pyzmq)
BuildRequires : pypi(qtpy)
BuildRequires : pypi(traitlets)

%description
# Jupyter QtConsole
![Windows tests](https://github.com/jupyter/qtconsole/workflows/Windows%20tests/badge.svg)
![Macos tests](https://github.com/jupyter/qtconsole/workflows/Macos%20tests/badge.svg)
![Linux tests](https://github.com/jupyter/qtconsole/workflows/Linux%20tests/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/jupyter/qtconsole/badge.svg?branch=master)](https://coveralls.io/github/jupyter/qtconsole?branch=master)
[![Documentation Status](https://readthedocs.org/projects/qtconsole/badge/?version=stable)](https://qtconsole.readthedocs.io/en/stable/)
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)

%package bin
Summary: bin components for the pypi-qtconsole package.
Group: Binaries
Requires: pypi-qtconsole-license = %{version}-%{release}

%description bin
bin components for the pypi-qtconsole package.


%package license
Summary: license components for the pypi-qtconsole package.
Group: Default

%description license
license components for the pypi-qtconsole package.


%package python
Summary: python components for the pypi-qtconsole package.
Group: Default
Requires: pypi-qtconsole-python3 = %{version}-%{release}

%description python
python components for the pypi-qtconsole package.


%package python3
Summary: python3 components for the pypi-qtconsole package.
Group: Default
Requires: python3-core
Provides: pypi(qtconsole)
Requires: pypi(ipykernel)
Requires: pypi(ipython_genutils)
Requires: pypi(jupyter_client)
Requires: pypi(jupyter_core)
Requires: pypi(pygments)
Requires: pypi(pyzmq)
Requires: pypi(qtpy)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-qtconsole package.


%prep
%setup -q -n qtconsole-5.3.2
cd %{_builddir}/qtconsole-5.3.2
pushd ..
cp -a qtconsole-5.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661792907
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-qtconsole
cp %{_builddir}/qtconsole-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-qtconsole/6b85326e6a68c099bbfa0e2c7d5ca15aa9763753 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-qtconsole

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-qtconsole/6b85326e6a68c099bbfa0e2c7d5ca15aa9763753

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
