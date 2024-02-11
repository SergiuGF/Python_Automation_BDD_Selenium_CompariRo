from behave import *

@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

"""@Login1"""
@when('I insert an unregistered email "{user}" in the mail input')
def step_impl(context, user):
    (context.login_page.set_unregistred_email(user))
@when('I insert a password "{pwd}"in the password input')
def step_impl(context, pwd):
    context.login_page.set_password(pwd)
@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()
@then('The error message is displayed')
def step_impl(context):
    context.login_page.is_error_message_displayed()
@then('The error message contains "{text}" message')
def step_impl(context, text):
    context.login_page.is_error_message_correct(text)

"""@Login2"""
@when('I insert " " in the mail input')
def step_impl(context):
    context.login_page.set_empty_email(" ")
@when('I click on the login button - Scenario 2')
def step_impl(context):
    context.login_page.click_login_button()
@then('Email error message is displayed - Scenario 2')
def step_impl(context):
    context.login_page.is_error_message_displayed()
@then('Email error text contains "{message}" message - Scenario 2')
def step_impl(context, message):
    context.login_page.is_error_message_correct(message)

"""@Login3"""
@when('I insert an valid email in the mail input')
def step_impl(context):
    context.login_page.set_valid_email("testingemail2352@gmail.com")
@when('I insert an valid password in the password input')
def step_impl(context):
    context.login_page.set_valid_password("Passfortesting123!")
@when('I click on the login button - Scenario 3')
def step_impl(context):
    context.login_page.click_login_button()
@then('I am redirected to account page "{account_page}"')
def step_impl(context, account_page):
    context.login_page.test_url_account(account_page)
