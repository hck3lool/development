*** Settings ***
Resource  ../resources.robot

Library  OperatingSystem


*** Keywords ***
Message "${msg}" should have been written to log-file
    ${text}=  Get File  ${PATH_LOG_FILE}  encoding_errors=ignore
    Should Contain
    ...    ${text}
    ...    ${msg}
    ${txt}=  Grep File  ${PATH_LOG_FILE}  ${msg}  encoding_errors=ignore
    Log Many  ${txt}
