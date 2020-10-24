Feature: Login

  Scenario Outline: this is the login tests
    Given I am at the CII page
    Given I am ozgur
    When I login with my <pin> and <password>
    Then I should see my PIN on the dashboard
    Examples:
      | pin                    | password |
      | ozgurgerilla@gmail.com | gogogo   |