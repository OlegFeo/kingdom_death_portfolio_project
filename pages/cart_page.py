from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):
    """ Класс содержащий локаторы и методы для корзины"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_button = '//input[@class="checkout-btn"]'
    product = '//span[@class="product-title"]'
    price = '//div[@class="theme-money"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods

    def product_assert(self, product):
        self.assert_word(self.get_product(), product)

    def price_assert(self, price):
        self.assert_word(self.get_price(), price)

    def product_confirmation(self, product, price):
        self.get_current_url()
        self.product_assert(product)
        self.price_assert(price)
        self.click_checkout_button()