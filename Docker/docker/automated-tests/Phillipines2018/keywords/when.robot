*** Settings ***
Resource          ../resources.robot

Library          Process


*** Keywords ***
User insert the correct pin in the keypad
    "StartupMachineInformation" screen should be shown
    User press "Menu" button
    "Challenge" screen should be shown
    User insert pin "${master_pin}" in the keypad
    "Challenge" screen should be shown