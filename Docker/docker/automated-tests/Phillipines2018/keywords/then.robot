*** Settings ***
Library          Process


*** Keywords ***
Election closes
    terminate process
    ...     election
    terminate all processes
    ...     kill=true