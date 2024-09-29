Feature: VSM Homepage
    Scenario: Login with correct credential
    Given When I on login page
    When I login with correct credential
    Then I shall redirect to Dashboard page