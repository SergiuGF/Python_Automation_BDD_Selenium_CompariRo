# This scenario no longer works because currently no products have been identified to be sold by Compari.ro


# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
#
# class CarPage(BasePage):
#     PRODUCT_PAGE = "https://www.compari.ro/cafetiere-filtre-de-cafea-c3174/philips/ep2236-40-p590842329/"
#     EXPAND_BUTTON = By.ID, 'c__expand_btn'
#     NEGRU_OPTION = By.CLASS_NAME, 'c-black__option'
#     FIRST_CUMPARA_BUTTON = By.XPATH, "//*[contains(@class, 'col-sm-5')]//*[contains(@class, 'add-to-cart')]"
#     SECOND_CUMPARA_BUTTON = By.XPATH, "(//*[contains(@class, 'add-to-cart')])[last()]"
#     SPRE_COS_BUTTON = By.CLASS_NAME, 'c-cart-confirm__button--cart'
#
#
#     def navigate_to_product_page(self, product_page):
#         self.go_to(product_page)
#         self.driver.maximize_window()
#     def click_expand_button(self):
#         self.click(self.EXPAND_BUTTON)
#     def click_negru_option(self):
#         self.click(self.NEGRU_OPTION)
#     def click_first_cumpara_button(self):
#         self.click(self.FIRST_CUMPARA_BUTTON)
#     def click_second_cumpara_button(self):
#         self.click(self.SECOND_CUMPARA_BUTTON)
#     def click_spre_cos_button(self):
#         self.click(self.SPRE_COS_BUTTON)
#     def is_product_displayed(self, product):
#         is_product_displayed = False
#         try:
#             product_name = self.driver.find_element(By.XPATH, f'//p[contains(text(),"{product}")]')
#             is_product_displayed = product_name.is_displayed()
#         except:
#             pass
#
#         assert is_product_displayed == True