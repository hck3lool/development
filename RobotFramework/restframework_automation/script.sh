#!/bin/bash

rm ${PWD}/results/logfile.log
export ROBOT_SYSLOG_FILE=${PWD}/results/logfile.log
export ROBOT_SYSLOG_LEVEL=DEBUG

robot --loglevel DEBUG:INFO --outputdir ${PWD}/results cases/requests.robot
