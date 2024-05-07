Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home Page
    Given launch the chrome browser
    When open the OrangeHRM Home Page
    Then verify the logo on the page
    And close browser