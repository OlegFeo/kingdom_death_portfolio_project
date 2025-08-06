import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from faker import Faker

faker = Faker("ru-RU")


class CheckoutPage(Base):
    """ Класс содержащий локаторы и методы для страницы оплаты"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    email = '//input[@placeholder="Email"]'
    first_name = '//input[@placeholder="First name"]'
    last_name = '//input[@placeholder="Last name"]'
    address = '//input[@placeholder="Address"]'
    city = '//input[@placeholder="City"]'
    postal_code = '//input[@placeholder="Postal code"]'
    phone = '//input[@placeholder="Phone"]'
    card = '//input[@placeholder="Card number"]'
    exp_month = '//input[@placeholder="Expiration date (MM / YY)"]'
    exp_year = '//input[@data-current-field="expiry"]'
    security_code = '//input[@placeholder="Security code"]'
    owner_name = '//input[@data-current-field="name"]'
    mobile_phone = '//input[@placeholder="Mobile phone number"]'
    pay = '//button[@id="checkout-pay-button"]'

    # Getters

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_card(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.card)))

    def get_exp_month(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exp_month)))

    def get_exp_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exp_year)))

    def get_security_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.security_code)))

    def get_owner_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.owner_name)))

    def get_mobile_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_phone)))

    def get_pay_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pay)))

    def get_product(self, product):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//p[contains(text(), "{product}")]')))

    def get_price(self, price):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'(//span[contains(text(), "{price}")])[1]')))


    # Actions

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_address(self, address):
        self.get_address().send_keys(address)
        print("Input address")

    def input_city(self, city):
        self.get_city().send_keys(city)
        print("Input city")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postalcode")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input phone")

    def input_card(self, card):
        iframe = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@name, "card-fields-number")]')))
        self.driver.switch_to.frame(iframe)
        self.get_card().send_keys(card)
        print("Input card")
        self.driver.switch_to.default_content()

    def input_exp_date(self, exp_date_month, exp_date_year):
        iframe = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@name, "card-fields-expiry")]')))
        self.driver.switch_to.frame(iframe)
        self.get_exp_month().send_keys(exp_date_month)
        self.get_exp_year().send_keys(exp_date_year)
        print("Input exp date")
        self.driver.switch_to.default_content()

    def input_security_code(self, security_code):
        iframe = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@name, "card-fields-verification_value")]')))
        self.driver.switch_to.frame(iframe)
        self.get_security_code().send_keys(security_code)
        print("Input security code")
        self.driver.switch_to.default_content()

    def input_owner_name(self, owner_name):
        iframe = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@name, "card-fields-name")]')))
        self.driver.switch_to.frame(iframe)
        self.get_owner_name().clear()
        self.get_owner_name().send_keys(owner_name)
        print("Input owner name")
        self.driver.switch_to.default_content()

    def input_mobile_phone(self, mobile_phone):
        self.get_mobile_phone().send_keys(mobile_phone)
        print("Input mobile phone")

    def click_pay_button(self):
        self.get_pay_button().click()
        print("Click pay button")

    # Methods

    def input_minimal_information(self, email, first_name, last_name, address, city, postal_code, phone, card, exp_date_month, exp_date_year,
                                  security_code, owner_name, mobile_phone):
        self.input_email(email)
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_address(address)
        self.input_city(city)
        self.input_postal_code(postal_code)
        self.input_phone(phone)
        self.input_card(card)
        self.input_exp_date(exp_date_month, exp_date_year)
        self.input_security_code(security_code)
        self.input_owner_name(owner_name)
        self.input_mobile_phone(mobile_phone)

    def payment_with_positive_information(self, product, price):
        self.get_product(product)
        self.get_price(price)
        self.input_minimal_information(email=faker.email(), first_name=faker.first_name(), last_name=faker.last_name(),
                                       address=faker.address(), city=faker.city(), postal_code="187015",
                                       phone=faker.numerify(text='9#########'),
                                       card="4242 4242 4242 4242", exp_date_month="11", exp_date_year="55",
                                       security_code="123", owner_name=faker.name(),
                                       mobile_phone=faker.numerify(text='9#########'))
        self.click_pay_button()