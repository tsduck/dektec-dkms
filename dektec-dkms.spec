Name:          dektec-dkms
Version:       %{version}
Release:       %{release}
Summary:       DKMS for Dektec device driver kernel modules
Group:         System Environment/Kernel
License:       BSD
URL:           http://www.dektec.com/downloads/SDK/
Vendor:        DekTec Digital Video B.V.
Source0:       dektec-dkms-%{version}.tgz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:     noarch
Requires:      dkms

%description
Provide the source code and DKMS setup for the kernel modules of the Dektec
device drivers. Each time the kernel is upgraded, the Dektec modules are
automatically recompiled. The provided drivers are Dta, DtaNw, Dtu.

Dektec is a manufacturer of PC add-on cards, USB devices, IP converters and
software for the professional digital-television market. Their products are
used for test and measurement and to build broadcast infrastructure.

This is an independent packaging of the Dektec original drivers.

# Disable debuginfo package.
%global debug_package %{nil}

%prep
%setup -q -n dektec-dkms-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/src $RPM_BUILD_ROOT/etc/udev/rules.d
cp -r dektec-%{version} $RPM_BUILD_ROOT/usr/src
install -m 644 51-dta.rules 51-dtu.rules $RPM_BUILD_ROOT/etc/udev/rules.d

%post
[[ -n $(/usr/sbin/dkms status | grep dektec | grep "%{version}" | wc -l) ]] && /usr/sbin/dkms add -m dektec -v "%{version}"
/usr/sbin/dkms build -m dektec -v "%{version}"
/usr/sbin/dkms install -m dektec -v "%{version}"
exit 0

%preun
/usr/sbin/dkms remove -m dektec -v "%{version}" --all
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/src/dektec-%{version}
/etc/udev/rules.d/51-dta.rules
/etc/udev/rules.d/51-dtu.rules
%doc Readme License
