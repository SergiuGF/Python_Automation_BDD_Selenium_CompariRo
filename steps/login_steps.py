from behave import *

@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()

"""Login1"""
@when('User inserts email "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('User inserts a password "{pwd}" in the password input')
def step_impl(context, pwd):
    context.login_page.set_password(pwd)
@when('User click on the login button')
def step_impl(context):
    context.login_page.click_login_button()
@then('The error message is displayed')
def step_impl(context):
    context.login_page.is_error_message_displayed()
@then('The error message contains "{error_msg_text}" text')
def step_impl(context, error_msg_text):
    context.login_page.is_log_error_message_correct(error_msg_text)

"""@Login2"""
@then('I am redirected to account page "{account_page}"')
def step_impl(context, account_page):
    context.login_page.test_url_account(account_page)
