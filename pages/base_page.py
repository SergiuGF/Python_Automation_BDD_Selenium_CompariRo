from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import Driver


class BasePage(Driver):
    def go_to(self, page):
        return self.driver.get(page)
    def find(self, locator):
        return self.driver.find_element(*locator)
    def find_multiple(self, locator):
        return self.driver.find_elements(*locator)
    def click(self, locator):
        self.find(locator).click()
    def type(self, locator, text):
        if text == "N/A":
            pass
        else:
            self.find(locator).send_keys(text)
    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()
    def get_text(self, locator):
        return self.find(locator).text
    def get_text_multiple(self, locator):
        return self.find_multiple(locator).text
    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)
    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if not checkbox_element.is_selected():
            self.click(checkbox_locator)
    def current_url(self):
        return self.driver.current_url
    def wait_for_element_visibility(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, selector)))
