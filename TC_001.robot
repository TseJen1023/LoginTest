*** Settings ***
Library    SeleniumLibrary
#scrum

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

Invalid Login
    Open Browser To Login Page
    Input Username    bbbb
    Input Password    eeee
    Submit Credentials
    Error Page Should Be Open
    [Teardown]    Close Browser


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    # add selenium implicit wait 5 seconds
    set browser implicit wait    5
    Title Should Be    Login Page
Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}
    set browser implicit wait    5
Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}
Submit Credentials
    Click Button    button
Right Page Should Be Open
    Title Should Be    right
    sleep    5
Error Page Should Be Open
    Title Should Be    error
    sleep    5
