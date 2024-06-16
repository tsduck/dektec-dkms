## Linux DKMS for Dektec device drivers

**IMPORTANT:** This project is now archived. Starting with version 2024.06.0,
the Dektec LinuxSDK includes its own DKMS installation and this specific project
is no longer necessary.

### About Dektec device drivers

[Dektec](http://www.dektec.com/) is a manufacturer of PC add-on cards, USB devices,
IP converters and software for the professional digital-television market. Their
products are used for test and measurement and to build broadcast infrastructure.

Dektec provides device drivers for Windows and Linux. See their comprehensive
[download](http://www.dektec.com/downloads/SDK/) page.

On Windows, WinSDK, the SDK and device drivers package, is a standard binary
installer which properly installs and configures the DTAPI and the device drivers.
There is nothing to add.

### Installing the drivers on Linux

On Linux systems, the Dektec device drivers are provided in source form only,
as part of the LinuxSDK package. On lab or production systems where the kernel
can be periodically updated, dealing with drivers in source form is not very handy.
Most Linux distros have an answer for this: DKMS, Dynamic Kernel Module Support.
The source code of the drivers are installed in `/usr/src` and the drivers are
automatically recompiled and reinstalled in case of kernel update.

The Dektec LinuxSDK package now provides its own DKMS installation. After downloading
the LinuxSDK archive from the [Dektec download page](http://www.dektec.com/downloads/SDK/),
expand it into some temporary directory. Everything is expanded under a root subdirectory
named `LinuxSDK`.

Important: Before installing the drivers, verify that your system is ready for DKMS.
On most distros, this means installing a package named `dkms` and a few dependencies.

To install the Dektec device drivers into the DKMS build system, use the following command:

```
sudo LinuxSDK/Drivers/Install
```

The command installs the drivers source code in `/usr/src/dektec-2024.06.0/`
(for version `2024.06.0`) and builds the drivers for the current kernel
in `/var/lib/dkms/dektec/2024.06.0/`. Each time the kernel will be upgraded,
the Dektec device drivers (and all drivers in the DKMS system) will be
automatically recompiled.

To remove the Dektec device drivers from the DKMS system, use the following command:

```
sudo LinuxSDK/Drivers/Uninstall
```
