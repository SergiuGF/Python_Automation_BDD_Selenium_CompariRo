from driver import Driver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.home_page import HomePage
from pages.cart_page import CarPage

def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.cart_page = CarPage()
def after_all(context):
    context.browser.close()


