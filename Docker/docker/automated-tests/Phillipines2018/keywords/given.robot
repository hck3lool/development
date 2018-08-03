*** Settings ***
Resource         ../resources.robot

Library          Process


*** Keywords ***
Machine starts
    start process
    ...    election     -w     800x480
    ...    alias=election