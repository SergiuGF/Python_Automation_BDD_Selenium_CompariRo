Feature: Test the functionality of the Login Page

  Background: Open Login Page
    Given I am on the Login Page

  @Login1
  Scenario Outline: Check that error message is displayed when user tries to login with invalid email address
    When User inserts email "<invalid_email>" in the email input
    When User inserts a password "<password>" in the password input
    When User click on the login button
    Then The error message is displayed
    Then The error message contains "<error_msg_text>" text

    Examples:
      | invalid_email                 | password | error_msg_text                                 |
      | email_neinregistrat1@host.com | password | Cu adresa de e-mail nu s-a creat inca cont.    |
      | N/A                           | password | Furnizarea adresei de e-mail este obligatorie! |

  @Login2
   Scenario: Check that user is redirected to account page when tries to login with an valid email and password
     When User inserts email "testingemail2352@gmail.com" in the email input
     When User inserts a password "Passfortesting123!" in the password input
     When User click on the login button
     Then I am redirected to account page "https://www.compari.ro/users/452083/#settings-account"
