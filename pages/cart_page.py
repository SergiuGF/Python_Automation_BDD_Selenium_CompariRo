from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class CarPage(BasePage):
    PRODUCT_PAGE = "https://www.compari.ro/cafetiere-filtre-de-cafea-c3174/philips/ep2236-40-p590842329/"
    EXPAND_BUTTON = By.ID, 'c__expand_btn'
    NEGRU_OPTION = By.CLASS_NAME, 'c-black__option'
    FIRST_CUMPARA_BUTTON = By.XPATH, "(//*[contains(@class, 'add-to-cart')])[3]"
    SECOND_CUMPARA_BUTTON = By.XPATH, "(//*[contains(@class, 'add-to-cart')])[last()]"
    SPRE_COS_BUTTON = By.CLASS_NAME, 'c-cart-confirm__button--cart'
    PRODUCT = By.CLASS_NAME, 'c-card__product'

    def navigate_to_product_page(self):
        self.go_to(self.PRODUCT_PAGE)
        self.driver.maximize_window()
    def click_expand_button(self):
        self.click(self.EXPAND_BUTTON)
    def click_negru_option(self):
        self.click(self.NEGRU_OPTION)
    def click_first_cumpara_button(self):
        self.click(self.FIRST_CUMPARA_BUTTON)
    def click_second_cumpara_button(self):
        self.click(self.SECOND_CUMPARA_BUTTON)
    def click_spre_cos_button(self):
        self.click(self.SPRE_COS_BUTTON)
    def is_product_displayed(self):
        assert self.is_element_displayed(self.PRODUCT)
