from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Payment_page(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finish_button = "//button[@id='finish']"

    # Getters

    def select_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions

    def click_finish_button(self):
        self.select_finish_button().click()
        print("Click finish button")

    # Methods

    def payment(self):
        self.get_current_url()
        self.click_finish_button()