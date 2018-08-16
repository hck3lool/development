#!/usr/bin/env bash

rmmod gadgetfs
rmmod g_mass_storage
rmmod usb_f_mass_storage
rmmod libcomposite
rmmod dummy-hcd
rmmod udc-core
echo " --> Modules removed successfuly"