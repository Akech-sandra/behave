Feature: User login

  Scenario: User logs in with valid credentials
    Given I am on the WordPress login page
    When I enter valid WordPress credentials
    Then I should be logged into the WordPress dashboard
