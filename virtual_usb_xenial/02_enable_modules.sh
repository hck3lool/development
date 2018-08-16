#!/usr/bin/env bash

main_path=$HOME/envir

modprobe gadgetfs
modprobe libcomposite
modprobe usb_f_mass_storage
modprobe udc-core
modprobe dummy-hcd
modprobe g_mass_storage file=$main_path/mass_storage_a.img,$main_path/mass_storage_b.img luns=2 stall=0 removable=y,y
echo " --> Modules enabled successfuly"
