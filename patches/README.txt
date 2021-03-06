This directory contains patches for different versions of the Dektec drivers.
There is at most one patch file for each version of the DKMS package. Such
a patch may be required when the Dektec drivers do not compile on a given
version of the kernel for instance.

Patch creation guidelines:

- Prepare the DKMS environment:

  $ ./build-dektec-dkms -v -p
  build-dektec-dkms: package version is 2019.11.0
  build-dektec-dkms: building DKMS structure in tmp/dektec-dkms-2019.11.0/dektec-2019.11.0

- Try to compile the drivers:

  $ VERSION=2019.11.0
  $ make -C tmp/dektec-dkms-$VERSION/dektec-$VERSION

- In case of errors, cleanup and duplicate the directory tree:

  $ make clean -C tmp/dektec-dkms-$VERSION/dektec-$VERSION
  $ cp -r tmp/dektec-dkms-$VERSION tmp/dektec-dkms-$VERSION.fixed

- Fix bugs in dektec-dkms-$VERSION.fixed. Make sure it compiles correctly. Be
  sure to modify the code so that it compiles on all versions of the kernel.

- Generate the patch file

  $ make clean -C tmp/dektec-dkms-$VERSION/dektec-$VERSION
  $ make clean -C tmp/dektec-dkms-$VERSION.fixed/dektec-$VERSION
  $ (cd tmp; diff -Naur dektec-dkms-$VERSION dektec-dkms-$VERSION.fixed) >patches/dektec-dkms-$VERSION.patch
