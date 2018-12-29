#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-oauthlib
Version  : 1.0.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/95/be/072464f05b70e4142cb37151e215a2037b08b1400f8a56f2538b76ca6205/requests-oauthlib-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/be/072464f05b70e4142cb37151e215a2037b08b1400f8a56f2538b76ca6205/requests-oauthlib-1.0.0.tar.gz
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

%description python3
python3 components for the requests-oauthlib package.


%prep
%setup -q -n requests-oauthlib-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542650964
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-oauthlib
cp LICENSE %{buildroot}/usr/share/package-licenses/requests-oauthlib/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-oauthlib/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
