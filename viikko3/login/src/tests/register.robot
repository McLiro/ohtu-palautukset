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
