*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Character
    Set Username  kalle
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Mismatching Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Too Short Username And Valid Password
    Set Username  kl
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Password Containing Only Lowercase Letters
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must not consist only of letters

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  kalle
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must not consist only of letters

Register With Username That Is Already In Use
    Create User  kalle  kalle123
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password
