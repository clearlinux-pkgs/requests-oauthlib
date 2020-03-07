#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-oauthlib
Version  : 1.2.0
Release  : 11
URL      : https://files.pythonhosted.org/packages/de/a2/f55312dfe2f7a344d0d4044fdfae12ac8a24169dc668bd55f72b27090c32/requests-oauthlib-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/a2/f55312dfe2f7a344d0d4044fdfae12ac8a24169dc668bd55f72b27090c32/requests-oauthlib-1.2.0.tar.gz
Summary  : OAuthlib authentication support for Requests.
Group    : Development/Tools
License  : ISC
Requires: requests-oauthlib-license = %{version}-%{release}
Requires: requests-oauthlib-python = %{version}-%{release}
Requires: requests-oauthlib-python3 = %{version}-%{release}
Requires: oauthlib
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : oauthlib
BuildRequires : requests
BuildRequires : requests-mock

%description
=========================================================

%package license
Summary: license components for the requests-oauthlib package.
Group: Default

%description license
license components for the requests-oauthlib package.


%package python
Summary: python components for the requests-oauthlib package.
Group: Default
Requires: requests-oauthlib-python3 = %{version}-%{release}

%description python
python components for the requests-oauthlib package.


%package python3
Summary: python3 components for the requests-oauthlib package.
Group: Default
Requires: python3-core
Provides: pypi(requests_oauthlib)
Requires: pypi(oauthlib)
Requires: pypi(requests)

%description python3
python3 components for the requests-oauthlib package.


%prep
%setup -q -n requests-oauthlib-1.2.0
cd %{_builddir}/requests-oauthlib-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583542932
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-oauthlib
cp %{_builddir}/requests-oauthlib-1.2.0/LICENSE %{buildroot}/usr/share/package-licenses/requests-oauthlib/44d0ccfd43c5941abf44e8e5dba5e198a1b4badd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-oauthlib/44d0ccfd43c5941abf44e8e5dba5e198a1b4badd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
