Feature: OrangeHRM Login

  Background: common steps
    """
    This block only for common steps purpose
    common file will be listed here.
    so, we should keeps all the common file here
    """


  Scenario: Login with valid credentials
    Given I am on the OrangeHRM login page
    When I enter username "admin" in the user field
    And I enter password "admin123" in the password field
    And I click the on Login button
    Then I should see the Dashboard page

  Scenario Outline: Login with multiple credentials
    Given I am on the OrangeHRM login page
    When I enter username "<username>" in the user field
    And I enter password "<password>" in the password field
    And I click the on Login button
    Then I should see the Dashboard page

    Examples:
      | username | password  |
      | admin    | admin123  |
      | admin12  | admin123  |