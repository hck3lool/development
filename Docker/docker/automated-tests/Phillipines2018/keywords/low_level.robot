*** Settings ***
Library           application_windows.ApplicationWindow


*** Keywords ***
User press "${button}" button
    press button     ${button}

"${screen}" screen should be shown
    wait for screen     ${screen}

User insert pin "${pin}" in the keypad
    insert pin number     ${pin}