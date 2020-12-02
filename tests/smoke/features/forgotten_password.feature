Feature: Great-magna Forgot Password

  Scenario: User should be able to reset password

    Given User is navigated to Login Page
    When User clicks on forgotten password
    When User enters "emailaddress" to reset password
    Then User receives an email with reset password link
#    When user enters new "password" and "confirm password" details

