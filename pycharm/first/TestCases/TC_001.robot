*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${LOGIN URL}  http://localhost:5000/login
${Browser}  Chrome


*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    aaaa
    Input Password    aaaa
    Submit Credentials
    Right Page Should Be Open
    [Teardown]    Close Browser


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Login Page
Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}
Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}
Submit Credentials
    Click Button    button
Right Page Should Be Open
    Title Should Be    right
