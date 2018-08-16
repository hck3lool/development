#!/usr/bin/env bash

apt-get update
apt-get -y install libssl-dev
apt-get -y --force-yes install dpkg-dev

unzip ubuntu-xenial.zip

mkdir $HOME/envir
main_path=$HOME/envir
cp -r ubuntu-xenial $main_path/

cd $main_path
apt-get update
cd ubuntu-*
cp /boot/config-$(uname -r) .config
cp /usr/src/linux-headers-$(uname -r)/Module.symvers .
echo "CONFIG_USB_DUMMY_HCD=m" >> .config

make oldconfig
make prepare
make scripts

make -j 4 M=drivers/usb/gadget

cp drivers/usb/gadget/legacy/gadgetfs.ko /lib/modules/$(uname -r)/kernel/drivers/usb/gadget/legacy/
cp drivers/usb/gadget/udc/dummy_hcd.ko /lib/modules/$(uname -r)/kernel/drivers/usb/gadget/udc/
cp drivers/usb/gadget/udc/udc-core.ko /lib/modules/$(uname -r)/kernel/drivers/usb/gadget/udc/
cp drivers/usb/gadget/legacy/g_mass_storage.ko /lib/modules/$(uname -r)/kernel/drivers/usb/gadget/legacy/
cp drivers/usb/gadget/libcomposite.ko /lib/modules/$(uname -r)/kernel/drivers/usb/gadget/
cp drivers/usb/gadget/function/usb_f_mass_storage.ko /lib/modules/$(uname -r)/kernel/drivers/usb/gadget/function/

depmod -a
echo " --> Modules created successfuly"

touch $main_path/mass_storage_a.img
touch $main_path/mass_storage_b.img

dd if=/dev/zero of=$main_path/mass_storage_a.img bs=1k count=4M
dd if=/dev/zero of=$main_path/mass_storage_b.img bs=1k count=4M
echo " --> Virtual files created"