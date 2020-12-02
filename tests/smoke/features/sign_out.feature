Feature: Sign out
  Scenario: Sign out from Home page after successful login
    Given User is on home page after login
    When User navigates to Avatar and click on sign out
    Then User should navigate to login page