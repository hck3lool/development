#!/usr/bin/env bash

function install_robotframework_dependencies() {
  local packages=(
    "html"
    "iso8601"
    "lxml"
    "mock"
    "pbkdf2"
    "psutil"
    "pycrypto"
    "PyUserInput"
    "robotframework"
    "robotframework-archivelibrary"
    "robotframework-debuglibrary"
    "robotframework-difflibrary"
  )
  for package in ${packages[@]}; do
    pip install ${package}
  done
}

function install_ldtp() {
  cd /tmp/
  git clone https://github.com/ldtp/ldtp2.git
  cd ldtp2
  python setup.py install
  cd -
  rm -rf /tmp/ldtp2

}

function main() {
  install_robotframework_dependencies
  install_ldtp
}

main
