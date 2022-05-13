Feature: Check Login Functionality

  Scenario: Users cannot login with null data
    Given User go to Login Page
    When User in login page
    Then Click Login
    And Verify if user cannot login and get error message

  Scenario: Users cannot login with username and password invalid
    Given User in login page
    When User input invalid username and password
    Then Click Login
    And Verify if user cannot login and get error message invalid

  Scenario: Users can click forgot password
    Given User in login page
    When User click forgot password
    Then Verify if user in forgot password page

  Scenario: Users cannot input invalid email in forgot password page
    Given User in forgot password page
    When User input invalid email
    Then Click submit
    And Verify if user get error message in forgot password page

  Scenario: Users can input valid email in forgot password page
    Given User in forgot password page
    When User input valid email
    Then Click submit
    And Verify if user can success submit

  Scenario: Users can input valid username and password
    Given User in success submit
    When Click Back to Login
    And Input valid username and password
    And Click Login
    Then Verify if user can login with valid data
