from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class StartPage(Base):
    """ Класс содержащий локаторы и методы для стартовой страницы"""

    url = 'https://kingdomdeath.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    shop = '//a[@href="https://shop.kingdomdeath.com"]'
    shop_check_word = '//span[text()="Shop now"]'

    # Getters

    def get_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop)))

    def get_shop_check_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_check_word)))

    # Actions

    def click_shop(self):
        self.get_shop().click()
        print("Click login button")

    # Methods

    def go_to_start_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

    def go_to_shop(self):
        self.click_shop()
        self.assert_word(self.get_shop_check_word(), "SHOP NOW")
        self.get_current_url()
        self.assert_url('https://shop.kingdomdeath.com/')
