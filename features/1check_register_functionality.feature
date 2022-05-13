Feature: Check Register Functionality

  Scenario: Users can open register page
    Given Open Stockbit
    When Click Register page
    Then Verify if users can redirect to register page

  Scenario: Users can choose register with email
    Given Users in register page
    When Users click register with email
    Then Verify user can click register with email

  Scenario: Users cannot register with null data
    Given User in Register form
    When Click Register
    Then Verify user cant register and get error message

  Scenario: Users can input name in register page
    Given User in Register form
    When input name
    Then Verify if user can input name

  Scenario: Users can input invalid email in register page
    Given User in Register form
    When input invalid email
    Then Verify if user can see error message email

  Scenario: Users cannot input with email not available
    Given User in Register form
    When input available email
    Then Verify if user can see error message email available

  Scenario: Users can input email with correct email format
    Given User in Register form
    When Input valid email
    Then Verify if user can input email

  Scenario: Users cannot input username with 3 character
    Given User in Register form
    When Input username with 2 character
    Then Verify if user can see error message username 3 character

  Scenario: Users cannot use the username that is used
    Given User in Register form
    When Input username that is used
    Then Verify if user can see error message username not available

  Scenario: Users can input username with username available
    Given User in Register form
    When Input username available
    Then Verify if user can input username

  Scenario: Users cannot input password with invalid confirm password
    Given User in Register form
    When Input correct password
    And Input incorrect confirm password
    Then Verify if user can see error message password

  Scenario: Users can input password with valid confirm password
    Given User in Register form
    When Input correct password
    And Input correct confirm password
    Then Verify if user can register

  Scenario: Users can input invalid phone number
    Given User in Phone Verification page
    When Input invalid phone number format
    Then Verify if user can see error message invalid phone number format

  Scenario: Users can input valid phone number
    Given User in Phone Verification page
    When Input valid phone number
    Then verify if user can send phone verification

  Scenario: Users cannot input invalid verification code
    Given User in Verification code
    When User input invalid code
    Then verify if user can see error message verification code