#!/bin/bash

cd ../main-files

#Preferences
cp storage.xml /etc/election/preferences/
cp security.xml /etc/election/preferences/
cp devices.xml /etc/election/preferences/

#Plugins
cp fake-devices.plugins.xml /etc/election/plugins/
cp philippines-pcos-configuration.plugins.xml /etc/election/plugins/
cp system-hash-initializer.plugins.xml /etc/election/plugins/
