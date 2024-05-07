Feature: OrangeHRM Login
  Scenario: Login with valid credentials
    Given I am on the OrangeHRM login page
    When I enter username "admin" in the user field
    And I enter password "admin123" in the password field
    And I click the on Login button
    Then I should see the Dashboard page