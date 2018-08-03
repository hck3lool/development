*** Settings ***
Documentation     Example test case using the gherkin syntax.
...               Concept Proof to integrate robot framework with PCOS Philippines

Resource          ../../resources.robot


*** Test Cases ***
User unblocks the keypad
     Given machine starts
     When user insert the correct pin in the keypad
     Then election closes