from behave import *

@given("I am on the Register Page")
def step_impl(context):
    context.register_page.navigate_to_register_page()

"""@Register1"""
@when('User inserts random email')
def step_impl(context):
    context.register_page.set_random_email()
@when('User inserts a password "{password}"')
def step_impl(context, password):
    context.register_page.set_password(password)
@when('User clicks on the register button')
def step_impl(context):
    context.register_page.click_register_button()
@then('Success message is displayed')
def step_impl(context):
    context.register_page.is_success_message_displayed()

"""@Register2"""
@when('User inserts empty email')
def step_impl(context):
    context.register_page.set_empty_email(" ")
@then('Error message is displayed')
def step_impl(context):
    context.register_page.error_message_is_displayed()
@then('Error message contains "{empty_error_text}"')
def step_impl(context, empty_error_text):
    context.register_page.is_reg_error_message_correct(empty_error_text)

"""@Register3"""
@when('User inserts empty password " "')
def step_impl(context):
    context.register_page.set_empty_password(' ')
