#!/usr/bin/env bash

( echo o; echo n; echo p; echo 1; echo ; echo; echo w; ) | fdisk /dev/sdb
mkfs.ext3 /dev/sdb1

( echo o; echo n; echo p; echo 1; echo ; echo; echo w; ) | fdisk /dev/sdc
mkfs.ext3 /dev/sdc1

echo " --> Partitions created"