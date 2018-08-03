#!/bin/bash

ELECTION_VERSION=$1
FRAMEWORK_VERSION=$2

function download_install_packages() {
  local packages=(
    "saes-cpp-framework-lib_${FRAMEWORK_VERSION}_amd64.deb"
    "election-base_${ELECTION_VERSION}_amd64.deb"
    "election-pcos_${ELECTION_VERSION}_amd64.deb"
    "election-philippines-pcos-configuration_${ELECTION_VERSION}_amd64.deb"
  )
  for package in ${packages[@]}; do
    wget http://10.4.13.108/at-packages/${package} -O /tmp/${package}
    dpkg -i /tmp/${package}
    rm -f /tmp/${package}
  done

}

function main() {
  download_install_packages
}

main "$@"