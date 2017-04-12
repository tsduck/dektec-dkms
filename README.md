## Linux DKMS for Dektec device drivers

### About Dektec device drivers

[Dektec](http://www.dektec.com/) is a manufacturer of PC add-on cards, USB devices,
IP converters and software for the professional digital-television market. Their
products are used for test and measurement and to build broadcast infrastructure.

Dektec provides device drivers for Windows and Linux. See their comprehensive
[download](http://www.dektec.com/downloads/SDK/) page.

On Windows, [WinSDK](http://www.dektec.com/products/SDK/DTAPI/Downloads/WinSDK.zip),
the SDK and device drivers package, is a standard binary installer which properly
installs and configures the DTAPI and the device drivers. There is nothing to add.

On Linux, on the other hand, the device drivers are provided in source form only,
as part of the [LinuxSDK](http://www.dektec.com/products/SDK/DTAPI/Downloads/LinuxSDK.tar.gz)
package. On lab or production systems where the kernel can be periodically updated,
dealing with drivers in source form is not very handy. Most Linux distros have
an answer for this: DKMS, Dynamic Kernel Module Support. The source code of the
drivers are installed in `/usr/src` and the drivers are automatically recompiled
and reinstalled in case of kernel update.

This project proposes scripts to create installable DKMS packages for Dektec
device drivers on most Linux distros. Installers can be created for Red Hat,
CentOS, Fedora (.rpm) or Ubuntu (.deb).

This project contains build scripts only. No original Dektec software is provided
here. The build scripts automatically download the original
[LinuxSDK](http://www.dektec.com/products/SDK/DTAPI/Downloads/LinuxSDK.tar.gz)
from the Dektec Web site prior to build the packages.

Disclaimer: The owner of this project is not and has never been affiliated to
DekTec Digital Video B.V. but is a long-time user of Dektec products, both on
Windows and Linux systems.

### Version identification

Currently, there are three different device drivers in the LinuxSDK package
named `Dta`, `DtaNw` and `Dtu`. Each driver has a distinct version number.
It is not possible to provide three different DKMS packages since these drivers
interact with each other in the kernel (at least `Dta` and `DtaNw`) and
contain common code. It is important that a consistent combination of drivers
is provided. To enforce this consistency, all three drivers are provided into
one single DKMS package.

The LinuxSDK package contains the application API (so-called *DTAPI*) in binary
form and all device drivers in source code form. The DTAPI also has its distinct
version number. Unfortunately, there is no global version number for the LinuxSDK
package, only a date. A LinuxSDK package is, for instance, named *Version Feb2017*.

Additionally, there is no unique URL per version of the LinuxSDK package. There is
only one single URL pointing to the latest version of the LinuxSDK package. But the
downloaded file has always the same name
[LinuxSDK.tar.gz](http://www.dektec.com/products/SDK/DTAPI/Downloads/LinuxSDK.tar.gz).
There is no real way to identify the name (*Feb2017* for instance) in the
downloaded file. We can only extract the distinct version numbers for DTAPI
and the various device drivers.

For each version of the LinuxSDK package, we produce one DKMS package.
As a compromise, we use the DTAPI version number to identify the DKMS package.

### License

The build scripts in this project are released under the terms of the license
which is commonly referred to as
"[BSD 2-Clause License](http://opensource.org/licenses/BSD-2-Clause)" or
"Simplified BSD License" or "FreeBSD License".

All Dektec software, including the drivers, are currently released under the
same BSD 2-Clause License. See the file named "License" in the
[LinuxSDK](http://www.dektec.com/products/SDK/DTAPI/Downloads/LinuxSDK.tar.gz)
package. The Dektec license file is included in the DKMS packages to comply with
the terms of this license.

### Build

Simply run the provided script:

```
build-dektec-dkms
```

The generated package is created in the subdirectory `packages`. On Fedora,
Red Hat Entreprise Linux, CentOS and other clones, the package is a `.rpm`
file. On Ubuntu systems, the package is a `.deb` file.

### Complete documentation of the build script

```
Build the Linux DKMS package for Dektec device drivers. The type of package
depends on the underlying operating system.

Usage: build-dektec-dkms [options]

Options:

  -c
  --clean
      Do not build anything, just cleanup downloaded and temporary files.

  -d
  --download
      Only download and expand the Dektec LinuxSDK. Do not build DKMS packages.

  -h
  --help
      Display this help text.

  -f
  --force
      Force a download of the Dektec LinuxSDK, even if it is already present.
      This makes sure that the latest version is used.

  --install
      Directly install Dektec DKMS on the current system. Do not create a
      package. This is useful on unsupported systems (no .rpm, no .deb).

  -k
  --keep
      Keep temporary files. By default, they are deleted.

  -o directory
  --output directory
     Directory for the created files. By default, use the current directory.

  -p
  --prepare
      Only prepare the DKMS file structure in the temporary directory.
      Do not build DKMS packages, do not clean up files.

  --uninstall
      Directly uninstall Dektec DKMS from the current system. Do not properly
      uninstall a package. This is useful on unsupported systems (no .rpm,
      no .deb).

  -u "url"
  --url "url"
     URL of the Dektec LinuxSDK. Default:
     http://www.dektec.com/products/SDK/DTAPI/Downloads/LinuxSDK.tar.gz

  -v
  --verbose
      Display verbose information.
```
