#!/bin/bash

cd ../packages

#Install dependencies
dpkg -i --force-all saes-cpp-framework-lib_*_amd64.deb election-base_*_amd64.deb election-pcos_*_amd64.deb election-philippines-pcos-configuration_*_amd64.deb
