#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3353C9CEF108B584 (mdroth@utexas.edu)
#
Name     : qemu
Version  : 3.1.0
Release  : 97
URL      : http://wiki.qemu-project.org/download/qemu-3.1.0.tar.xz
Source0  : http://wiki.qemu-project.org/download/qemu-3.1.0.tar.xz
Source99 : http://wiki.qemu-project.org/download/qemu-3.1.0.tar.xz.sig
Summary  : A lightweight multi-platform, multi-architecture disassembly framework
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+ GPL-3.0 LGPL-2.0+ LGPL-2.1 MIT
Requires: qemu-bin = %{version}-%{release}
Requires: qemu-data = %{version}-%{release}
Requires: qemu-libexec = %{version}-%{release}
Requires: qemu-locales = %{version}-%{release}
Requires: qemu-setuid = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-qmake
BuildRequires : ceph-dev
BuildRequires : curl-dev
BuildRequires : flex
BuildRequires : glib-dev
BuildRequires : gtk3
BuildRequires : gtk3-dev
BuildRequires : jemalloc-dev
BuildRequires : libaio-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libiscsi
BuildRequires : libiscsi-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libseccomp-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : numactl-dev
BuildRequires : snappy-dev
BuildRequires : spice
BuildRequires : spice-dev
BuildRequires : spice-protocol
BuildRequires : usbredir-dev
BuildRequires : util-linux-dev
BuildRequires : zlib-dev
Patch1: configure.patch

%description
Capstone is a disassembly framework with the target of becoming the ultimate
disasm engine for binary analysis and reversing in the security community.

%package bin
Summary: bin components for the qemu package.
Group: Binaries
Requires: qemu-data = %{version}-%{release}
Requires: qemu-libexec = %{version}-%{release}
Requires: qemu-setuid = %{version}-%{release}

%description bin
bin components for the qemu package.


%package data
Summary: data components for the qemu package.
Group: Data

%description data
data components for the qemu package.


%package extras
Summary: extras components for the qemu package.
Group: Default

%description extras
extras components for the qemu package.


%package libexec
Summary: libexec components for the qemu package.
Group: Default

%description libexec
libexec components for the qemu package.


%package locales
Summary: locales components for the qemu package.
Group: Default

%description locales
locales components for the qemu package.


%package setuid
Summary: setuid components for the qemu package.
Group: Default

%description setuid
setuid components for the qemu package.


%prep
%setup -q -n qemu-3.1.0
%patch1 -p1
pushd ..
cp -a qemu-3.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547110034
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-sdl \
--enable-avx2 \
--enable-gtk \
--enable-vnc \
--enable-kvm \
--disable-strip \
--target-list='i386-softmmu x86_64-softmmu i386-linux-user x86_64-linux-user' \
--enable-spice \
--enable-rbd \
--extra-cflags="-O3" \
--enable-attr \
--enable-cap-ng \
--enable-virtfs \
--enable-vhost-net \
--enable-usb-redir \
--python=/usr/bin/python \
--enable-seccomp \
--enable-linux-aio \
--enable-tpm \
--enable-opengl \
--enable-libiscsi \
--enable-coroutine-pool \
--enable-jemalloc \
--enable-numa
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --disable-sdl \
--enable-avx2 \
--enable-gtk \
--enable-vnc \
--enable-kvm \
--disable-strip \
--target-list='i386-softmmu x86_64-softmmu i386-linux-user x86_64-linux-user' \
--enable-spice \
--enable-rbd \
--extra-cflags="-O3" \
--enable-attr \
--enable-cap-ng \
--enable-virtfs \
--enable-vhost-net \
--enable-usb-redir \
--python=/usr/bin/python \
--enable-seccomp \
--enable-linux-aio \
--enable-tpm \
--enable-opengl \
--enable-libiscsi \
--enable-coroutine-pool \
--enable-jemalloc \
--enable-numa
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1547110034
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
%find_lang qemu

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/qemu-img
/usr/bin/haswell/ivshmem-client
/usr/bin/haswell/ivshmem-server
/usr/bin/haswell/qemu-edid
/usr/bin/haswell/qemu-ga
/usr/bin/haswell/qemu-i386
/usr/bin/haswell/qemu-img
/usr/bin/haswell/qemu-io
/usr/bin/haswell/qemu-keymap
/usr/bin/haswell/qemu-nbd
/usr/bin/haswell/qemu-pr-helper
/usr/bin/haswell/qemu-system-i386
/usr/bin/haswell/qemu-system-x86_64
/usr/bin/haswell/qemu-x86_64
/usr/bin/haswell/virtfs-proxy-helper
/usr/bin/ivshmem-client
/usr/bin/ivshmem-server
/usr/bin/qemu-edid
/usr/bin/qemu-ga
/usr/bin/qemu-i386
/usr/bin/qemu-io
/usr/bin/qemu-keymap
/usr/bin/qemu-nbd
/usr/bin/qemu-pr-helper
/usr/bin/qemu-system-i386
/usr/bin/qemu-system-x86_64
/usr/bin/qemu-x86_64
/usr/bin/virtfs-proxy-helper

%files data
%defattr(-,root,root,-)
/usr/share/qemu/QEMU,cgthree.bin
/usr/share/qemu/QEMU,tcx.bin
/usr/share/qemu/bamboo.dtb
/usr/share/qemu/bios-256k.bin
/usr/share/qemu/bios.bin
/usr/share/qemu/canyonlands.dtb
/usr/share/qemu/efi-e1000.rom
/usr/share/qemu/efi-e1000e.rom
/usr/share/qemu/efi-eepro100.rom
/usr/share/qemu/efi-ne2k_pci.rom
/usr/share/qemu/efi-pcnet.rom
/usr/share/qemu/efi-rtl8139.rom
/usr/share/qemu/efi-virtio.rom
/usr/share/qemu/efi-vmxnet3.rom
/usr/share/qemu/hppa-firmware.img
/usr/share/qemu/keymaps/ar
/usr/share/qemu/keymaps/bepo
/usr/share/qemu/keymaps/common
/usr/share/qemu/keymaps/cz
/usr/share/qemu/keymaps/da
/usr/share/qemu/keymaps/de
/usr/share/qemu/keymaps/de-ch
/usr/share/qemu/keymaps/en-gb
/usr/share/qemu/keymaps/en-us
/usr/share/qemu/keymaps/es
/usr/share/qemu/keymaps/et
/usr/share/qemu/keymaps/fi
/usr/share/qemu/keymaps/fo
/usr/share/qemu/keymaps/fr
/usr/share/qemu/keymaps/fr-be
/usr/share/qemu/keymaps/fr-ca
/usr/share/qemu/keymaps/fr-ch
/usr/share/qemu/keymaps/hr
/usr/share/qemu/keymaps/hu
/usr/share/qemu/keymaps/is
/usr/share/qemu/keymaps/it
/usr/share/qemu/keymaps/ja
/usr/share/qemu/keymaps/lt
/usr/share/qemu/keymaps/lv
/usr/share/qemu/keymaps/mk
/usr/share/qemu/keymaps/modifiers
/usr/share/qemu/keymaps/nl
/usr/share/qemu/keymaps/nl-be
/usr/share/qemu/keymaps/no
/usr/share/qemu/keymaps/pl
/usr/share/qemu/keymaps/pt
/usr/share/qemu/keymaps/pt-br
/usr/share/qemu/keymaps/ru
/usr/share/qemu/keymaps/sl
/usr/share/qemu/keymaps/sv
/usr/share/qemu/keymaps/th
/usr/share/qemu/keymaps/tr
/usr/share/qemu/kvmvapic.bin
/usr/share/qemu/linuxboot.bin
/usr/share/qemu/linuxboot_dma.bin
/usr/share/qemu/multiboot.bin
/usr/share/qemu/openbios-ppc
/usr/share/qemu/openbios-sparc32
/usr/share/qemu/openbios-sparc64
/usr/share/qemu/palcode-clipper
/usr/share/qemu/petalogix-ml605.dtb
/usr/share/qemu/petalogix-s3adsp1800.dtb
/usr/share/qemu/ppc_rom.bin
/usr/share/qemu/pxe-e1000.rom
/usr/share/qemu/pxe-eepro100.rom
/usr/share/qemu/pxe-ne2k_pci.rom
/usr/share/qemu/pxe-pcnet.rom
/usr/share/qemu/pxe-rtl8139.rom
/usr/share/qemu/pxe-virtio.rom
/usr/share/qemu/qemu-icon.bmp
/usr/share/qemu/qemu_logo_no_text.svg
/usr/share/qemu/qemu_vga.ndrv
/usr/share/qemu/s390-ccw.img
/usr/share/qemu/s390-netboot.img
/usr/share/qemu/sgabios.bin
/usr/share/qemu/skiboot.lid
/usr/share/qemu/slof.bin
/usr/share/qemu/spapr-rtas.bin
/usr/share/qemu/trace-events-all
/usr/share/qemu/u-boot-sam460-20100605.bin
/usr/share/qemu/u-boot.e500
/usr/share/qemu/vgabios-bochs-display.bin
/usr/share/qemu/vgabios-cirrus.bin
/usr/share/qemu/vgabios-qxl.bin
/usr/share/qemu/vgabios-ramfb.bin
/usr/share/qemu/vgabios-stdvga.bin
/usr/share/qemu/vgabios-virtio.bin
/usr/share/qemu/vgabios-vmware.bin
/usr/share/qemu/vgabios.bin

%files extras
%defattr(-,root,root,-)
/usr/bin/qemu-img

%files libexec
%defattr(-,root,root,-)
%exclude /usr/libexec/qemu-bridge-helper

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/libexec/qemu-bridge-helper

%files locales -f qemu.lang
%defattr(-,root,root,-)

