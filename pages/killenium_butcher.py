from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class KillenniumButcher(Base):
    """ Класс содержащий локаторы и методы для страницы Killenium Butcher"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart = '//button[@name="add"]'
    view_cart = '//a[@class="button alt"]'

    # Getters

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_view_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.view_cart)))

    # Actions

    def click_cart(self):
        self.get_add_to_cart().click()
        print("Click add to cart")

    def click_view_cart(self):
        self.get_view_cart().click()
        print("Click view cart")
        self.get_current_url()
        self.assert_url('https://shop.kingdomdeath.com/cart')

    # Methods

    def go_to_cart(self):
        self.scroll_down(0, 1000)
        self.click_cart()
        self.click_view_cart()
