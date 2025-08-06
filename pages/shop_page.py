from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class ShopPage(Base):
    """ Класс содержащий локаторы и методы для страницы магазина"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_killennium_butcher = '//a[@aria-label="Vignette of Death: Killennium Butcher"]'
    killennium_butcher_check_word = '//h1[contains(text(), "KILLENNIUM BUTCHER")]'

    # Getters

    def get_product_killenium_butcher(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_killennium_butcher)))

    def get_killenium_butcher_check_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.killennium_butcher_check_word)))

    # Actions

    def select_product_killenium_butcher(self):
        self.scroll_down(0, 600)
        self.get_product_killenium_butcher().click()
        print("Click on product killenium butcher")

    # Methods

    def go_to_product_killenium_butcher(self):
        self.select_product_killenium_butcher()
        self.assert_word(self.get_killenium_butcher_check_word(), "KILLENNIUM BUTCHER")
        self.get_current_url()
        self.assert_url('https://shop.kingdomdeath.com/products/vignette-of-death-killennium-butcher')
