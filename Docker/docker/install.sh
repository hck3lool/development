#!/bin/bash

readonly COLOR_RED="\033[0;31m"
readonly COLOR_YELLOW="\033[1;33m"
readonly COLOR_GREEN="\033[0;32m"
readonly COLOR_CYAN="\033[0;36m"
readonly COLOR_NONE="\e[0m"

OUT="> /dev/null 2>&1"

# Echo functions
function print_error_message() {
  local message=$1
  echo -e "${COLOR_RED}E: ${message}${COLOR_NONE}"
  exit 1
}

function print_status_message() {
  local message=$1
  echo -e "${COLOR_CYAN}I: ${message}${COLOR_NONE}"
}

function print_warning_message() {
  local message=$1
  echo -e "${COLOR_CYAN}W: ${message}${COLOR_NONE}"
}

function validate_root_user () {
  if [[ ${EUID} -ne 0 ]]; then
    print_error_message "Root permission are required. Please run $0 using sudo"
  fi
}

function install_dependencies() {
  print_status_message "Installing dependencies"
  if [[ -f "dependencies.sh" ]]; then
    source "dependencies.sh"
    local var=0
    local packages
    if [[ -n ${DEPENDENCIES_PACKAGES} ]]; then
      for package in ${DEPENDENCIES_PACKAGES[@]}; do
        local installation=($(dpkg -l | grep ${package} | head -n1))
        if [[ ${installation[0]} == "ii" ]] && [[ ${installation[1]} == ${package} ]]; then
          echo "Package ${package} already installed"
        else
          packages[var]=${package}
          ((var++))
        fi
      done
      if [[ ${#packages[@]} -gt 0 ]]; then
        apt-get update
        for package in ${packages[@]}; do
          apt-get install --yes --no-install-recommends ${package}
        done
      fi

    else
      print_warning_message "Dependencies packages variable doesn't found"
    fi
  fi
}

function install_docker() {
  print_status_message "Installing docker"
  print_status_message "Validate installation"
  local installation=($(dpkg -l | grep docker | head -n1))
  if [[ ${installation[0]} == "ii" ]]  && [[ ${installation[1]} == "docker" ]]; then
    print_status_message "Docker already installed"
  else
    print_status_message "Installing docker"
    curl -sSL https://get.docker.com/ | sh
  fi
}

function build_docker_file() {
  print_status_message "Build docker container"
  docker build -t "phillipines" ./
}

function main() {
  validate_root_user
  install_dependencies
  install_docker
  build_docker_file

}

main