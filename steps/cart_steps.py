from behave import *

@given('I am on the product page "{product_page}"')
def step_impl(context, product_page):
    context.cart_page.navigate_to_product_page(product_page)
@when('I click on the first Cumpara button')
def step_impl(context):
    context.cart_page.click_first_cumpara_button()
@when('I click on the second Cumpara button')
def step_impl(context):
    context.cart_page.click_second_cumpara_button()
@when('I click on the Spre cos button')
def step_impl(context):
    context.cart_page.click_spre_cos_button()
@then('the "{product_name}" product is displayed')
def step_impl(context, product_name):
    context.cart_page.is_product_displayed(product_name)