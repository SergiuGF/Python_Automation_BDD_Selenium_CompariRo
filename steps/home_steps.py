from behave import *

@given('I am on the Home Page')
def step_impl(context):
    context.home_page.navigate_to_home_page()

"""@Search1"""
@when('I click on the Search Bar')
def step_impl(context):
    context.home_page.click_search_bar()
@when('I insert ”{product_name}” in the Search Bar')
def step_impl(context, product_name):
    context.home_page.search_for_products(product_name)
@when('I click Search button')
def step_impl(context):
    context.home_page.click_search_button()
@then('At least 10 products are displayed')
def step_impl(context):
    context.home_page.check_product_quantity()

"""@Filter"""
@when('I click on the Telefoane mobile - under Electronice tab')
def step_impl(context):
    context.home_page.click_mobile()
@when('I click Valori individuale - under Pret tab')
def step_impl(context):
    context.home_page.click_value()
@when('I set the min value at "{min_value}"')
def step_impl(context, min_value):
    context.home_page.set_min_value(min_value)
@when('I set the max value at "{max_value}"')
def step_impl(context, max_value):
    context.home_page.set_max_value(max_value)
@when('I click ok button - under Pret tab')
def step_impl(context):
    context.home_page.click_ok_button()
@then('All products displayed are between "{min_price}" and "{max_price}" lei')
def step_impl(context, min_price, max_price):
    context.home_page.check_product_prices(min_price, max_price)

"""@Test_URL"""
@when('I click on the Cart button')
def step_impl(context):
    context.home_page.click_cart_page()
@then('I am redirected to the Cart Page "{expected_URL}"')
def step_impl(context, expected_URL):
    context.home_page.test_url(expected_URL)

"""@Comparatie"""
@when('I click on the Aparat foto button')
def step_impl(context):
    context.home_page.click_aparat_foto_page()
@when('I click Comparare checkbox')
def step_impl(context):
    context.home_page.check_comparare()
@when('I click on the Comparatie button')
def step_impl(context):
    context.home_page.click_comparatie()
@then('The selected product is displayed')
def step_impl(context):
    context.home_page.is_selected_product_displayed()