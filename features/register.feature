Feature: Test the functionality of the Register Page

  Background: Open Register Page
    Given I am on the Register Page

   @Register1
   Scenario: Check that success message is displayed when the user registers with a new email
     When User inserts random email
     When User inserts a password "Password8910"
     When User clicks on the register button
     Then Success message is displayed

   @Register2
   Scenario: Check that error message is displayed when the user enters empty email address
    When User inserts empty email
    When User clicks on the register button
    Then Error message is displayed
    Then Error message contains "Completarea campului este obligatorie!"

   @Register3
   Scenario: Check that error message is displayed when the user enters empty password input
    When User inserts random email
    When User inserts empty password " "
    When User clicks on the register button
    Then Error message is displayed
    Then Error message contains "Completarea campului este obligatorie!"