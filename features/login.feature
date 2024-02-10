Feature: Test the functionality of the Login Page

  Background: Open Login Page
    Given I am on the Login Page

   @Login1
   Scenario Outline: Check "Cu adresa de e-mail nu s-a creat inca cont." message is displayed when the user tries to login with an unregistered email
     When I insert an unregistered email "<unregistered_email>" in the mail input
     When I insert a password "<password>"in the password input
     When I click on the login button
     Then The error message is displayed
     Then The error message contains "Cu adresa de e-mail nu s-a creat inca cont." message

     Examples:
       | unregistered_email            | password  |
       | email_neinregistrat1@host.com | password1 |
       | email_neinregistrat2@host.com | password2 |
       | email_neinregistrat3@host.com | password3 |
       | email_neinregistrat4@host.com | password4 |

   @Login2
   Scenario: Check that "Furnizarea adresei de e-mail este obligatorie!" message is displayed when the user enters empty email adress
     When I insert " " in the mail input
     When I click on the login button - Scenario 2
     Then Email error message is displayed - Scenario 2
     Then Email error text contains "Furnizarea adresei de e-mail este obligatorie!" message - Scenario 2

    @Login3
   Scenario: Check that you are redirected to account page when the user tries to login with an valid email and password
     When I insert an valid email in the mail input
     When I insert an valid password in the password input
     When I click on the login button - Scenario 3
     Then I am redirected to account page "https://www.compari.ro/users/452083/#settings-account"
