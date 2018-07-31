*** Settings ***
Resource  ../resources.robot

Library  BuiltIn


*** Keywords ***
A url "${test_url}"
    [Documentation]  GET: The url model is: http://{IP_REST_SERVER:{PORT}}/v1/diff/{ID}/
    ...              parameter ID: should be any natural number
    ...              example: http://10.4.13.147:8000/v1/diff/7/

    ...              POST: The url model is: http://{IP_REST_SERVER:{PORT}}/v1/diff/{ID}/{SIDE}/
    ...              parameter ID: should be any natural number
    ...              parameter SIDE: should be "right" or "left"
    ...              example: http://10.4.13.147:8000/v1/diff/7/right/
    set suite variable  ${test_url}

A json url "${json_data}"
    set suite variable  ${json_data}
