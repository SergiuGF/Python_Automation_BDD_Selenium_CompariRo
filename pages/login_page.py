from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://www.compari.ro/login/"
    EMAIL_INPUT = (By.NAME, "uname")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-submit")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)
        self.driver.maximize_window()

    """@Login1"""
    def set_unregistred_email(self, user):
        self.type(self.EMAIL_INPUT, user)
    def set_password(self, pwd):
        self.type(self.PASSWORD_INPUT, pwd)
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
    def is_error_message_displayed(self):
        assert self.is_element_displayed(self.ERROR_MESSAGE)
    def get_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    """@Login2"""
    def set_empty_email(self, text):
        self.type(self.EMAIL_INPUT, text)
    # next steps are the same as in the previous scenario

    """@Login3"""
    def set_valid_email(self, text):
        self.type(self.EMAIL_INPUT, text)
    def set_valid_password(self, text):
        self.type(self.PASSWORD_INPUT, text)
    # Third step is the same as in the previous scenario (click_login_button)
    def test_url(self):
        current_url = self.current_url()
        return current_url




