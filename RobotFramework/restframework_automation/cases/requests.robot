*** Settings ***
Resource  ../resources.robot


*** Test Cases ***
Get request successful
    [Tags]  GET
    [Documentation]  This test case validates the get method be successful
    Given a url "http://localhost:8000/v1/diff/6/"
    When user gets request from url
    Then message "The get request was successful" should have been written to log-file

Get request invalid url
    [Tags]  GET
    [Documentation]  This test case validates the behavior when uses a invalid url
    Given a url "http://localhost:8000/v1/dif"
    When user gets request from a invalid url
    Then message "Checks the url name is valid" should have been written to log-file

Get request when do not exist documents
    [Tags]  GET
    [Documentation]  This test case validates the behavior (GET) when not exist documents in the servers
    Given a url "http://localhost:8000/v1/diff/78/"
    When user gets request from url without documents on the servers
    Then message "Unable compare the documents" should have been written to log-file

Post request successful
    [Tags]  POST
    [Documentation]  This test case validates the post method be successful
    Given a url "http://localhost:8000/v1/diff/7/left/"
    And a json url "{"data":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXNzYWdlIjoia2FrYXJvdG8ifQ.y9pMhKSRFu9YIc1pxLktUytbg5kk5yJylosXl5erJw0"}"
    When user posts request from url
    Then message "The post request was successful" should have been written to log-file

Post request invalid key
    [Tags]  POST
    [Documentation]  This test validates the behavior when a data contains a invalid key
    Given a url "http://localhost:8000/v1/diff/7/left/"
    And a json url "{"data":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsbWFvIjoia2FrYXJvdG8ifQ.PzKS7swGuNH50CCEBqfwQ-ktPSjI5JQ91zeiAgCju6I"}"
    When user posts request when json key not exist
    Then message "Checks the data contains the key 'message'" should have been written to log-file

Invalid data
    [Tags]  POST
    [Documentation]  This test case validates the key value in the json url
    Given a url "http://localhost:8000/v1/diff/5/left/"
    And a json url "{"data":"dfguhdguehudhgudhgudhkghdfkguhdkuadshaygdtaegdyasgdytasdfeytagvdyuaeg376567trg4fywfvbsjf"}"
    When user validates the json key value
    Then message "The encoded token could not be verified" should have been written to log-file

Validate equals strings
    [Tags]  GET
    [Documentation]  This test case validates if two strings are equals
    Given a url "http://localhost:8000/v1/diff/1/"
    When equals strings are verified
    Then message "The strings are equals" should have been written to log-file

Validate differents strings
    [Tags]  GET
    [Documentation]  This test case validates if two strings are differents
    Given a url "http://localhost:8000/v1/diff/6/"
    When differents strings are verified
    Then message "The strings do not equals" should have been written to log-file

Post request invalid url
    [Tags]  POST
    [Documentation]  This test case validates the behavior (POST) when uses a invalid url
    Given a url "http://localhost:8000/v1/diff/7/center/"
    And a json url "{"data":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsbWFvIjoia2FrYXJvdG8ifQ.PzKS7swGuNH50CCEBqfwQ-ktPSjI5JQ91zeiAgCju6I"}"
    When user posts request from a invalid url
    Then message "Checks the url name is valid" should have been written to log-file