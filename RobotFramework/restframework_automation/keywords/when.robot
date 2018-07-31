*** Settings ***
Resource  ../resources.robot

Library  ../libraries/configuration.py
Library  Collections
Library  BuiltIn
Library  OperatingSystem


*** Keywords ***
User gets request from url
    ${result}=  get request
                ...  ${test_url}
    should be equal  ${result}  ${200}
    create file  logfile.txt  The get request was successful

User gets request from a invalid url
    ${result}=  get request
                ...  ${test_url}
    should not be equal  ${result}  ${200}
    create file  logfile.txt  Checks the url name is valid

User gets request from url without documents on the servers
    ${result}=  get request
                ...  ${test_url}
    dictionary should contain key  ${result}  FileError
    create file  logfile.txt  Unable compare the documents

User posts request from url
    ${result}=  post request
                ...  ${test_url}
                ...  ${json_data}
    should be equal  ${result}  ${200}
    create file  logfile.txt  The post request was successful

User posts request when json key not exist
    ${result}=  post request
                ...  ${test_url}
                ...  ${json_data}
    dictionary should contain key  ${result}  KeyError
    create file  logfile.txt  Checks the data contains the key 'message'

Equals strings are verified
    ${result}=  get evaluate request
                ...   ${test_url}
    should be equal  ${result}  false
    create file  logfile.txt  The strings are equals

Differents strings are verified
    ${result}=  get evaluate request
                ...   ${test_url}
    should be equal  ${result}  true
    create file  logfile.txt  The strings do not equals

User validates the json key value
    ${result}=  post request
                ...  ${test_url}
                ...  ${json_data}
    dictionary should contain key  ${result}  JWTError
    create file  logfile.txt  The encoded token could not be verified

User posts request from a invalid url
    ${result}=  post request
                ...  ${test_url}
                ...  ${json_data}
    should not be equal  ${result}  ${200}
    create file  logfile.txt  Checks the url name is valid