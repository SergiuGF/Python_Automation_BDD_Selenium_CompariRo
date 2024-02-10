from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
import re


class HomePage(BasePage):
    HOME_PAGE_URL = "https://www.compari.ro/"
    SEARCH_BAR = By.CLASS_NAME, "c-search__input"
    SEARCH_BUTTON = By.CLASS_NAME, "c-search__button"
    PRODUCTS = By.CLASS_NAME, "product-box"
    MOBILE_TAB = By.LINK_TEXT, "Telefoane mobile"
    PRICE_VALUE = By.XPATH, '//*[@id="morefilter-pret"]/a/span[1]'
    MIN_VALUE = By.NAME, "pret_minValue"
    MAX_VALUE = By.NAME, "pret_maxValue"
    OK_BUTTON = By.XPATH, '//*[@id="cf_pret"]/span[2]/a'
    PRODUCT_PRICES = By.CLASS_NAME, "price"
    CART_PAGE = By.CSS_SELECTOR, '#header-cart-icon > svg'
    APARAT_FOTO_PAGE = By.LINK_TEXT, 'Aparat foto'
    COMPARARE_CHECKBOX = By.XPATH, '//*[@id="product-list"]/div[4]/div[3]/div[1]/div[1]/div[2]/a/span[1]'
    COMPARATIE_BUTTON = By.ID, 'header-button-comparison'
    SELECTED_PRODUCT = By.CLASS_NAME, 'product-wrapper'

    def navigate_to_home_page(self):
        self.go_to(self.HOME_PAGE_URL)
        self.driver.maximize_window()

    """@Search1"""
    def click_search_bar(self):
        self.click(self.SEARCH_BAR)
    def search_for_products(self, text):
        self.type(self.SEARCH_BAR, text)
    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
    def check_product_quantity(self):
        found_products = self.find_multiple(self.PRODUCTS)
        assert len(found_products) >=10

    """@Filter"""
    def click_mobile(self):
        self.click(self.MOBILE_TAB)
    def click_value(self):
        self.click(self.PRICE_VALUE)
    def set_min_value(self, text):
        self.type(self.MIN_VALUE, text)
    def set_max_value(self, text):
        self.type(self.MAX_VALUE, text)
    def click_ok_button(self):
        self.click(self.OK_BUTTON)
        sleep(2)
    def check_product_prices(self):
        product_prices_text = [price.text for price in self.find_multiple(self.PRODUCT_PRICES)]
        prices_list = [re.sub(r'[^\d,]', '', item) for item in product_prices_text if item.strip()]
        prices_list_int = [int(item.split(',')[0]) for item in prices_list]
        for price in prices_list_int:
            assert price >= 1000 and price <= 2000

    """@Test_URL"""
    def click_cart_page(self):
        self.click(self.CART_PAGE)

    def test_url(self,expected_URL):
        current_url = self.current_url()
        assert current_url == expected_URL

    """@Comparatie"""
    def click_aparat_foto_page(self):
        self.click(self.APARAT_FOTO_PAGE)
    def check_comparare(self):
        self.check_checkbox(self.COMPARARE_CHECKBOX)
    def click_comparatie(self):
        self.click(self.COMPARATIE_BUTTON)
    def is_selected_product_displayed(self):
        self.wait_for_elemement(By. CLASS_NAME,'product-wrapper')
        self.click(self.SELECTED_PRODUCT)
        assert self.is_element_displayed(self.SELECTED_PRODUCT)
