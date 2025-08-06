import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.killenium_butcher import KillenniumButcher
from pages.shop_page import ShopPage
from pages.start_page import StartPage


@pytest.mark.order(1)
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    print("Start test Killennium Butcher")

    """Тестовые данные"""
    product = "Vignette of Death: Killennium Butcher"
    price = "$100.00"

    start = StartPage(driver)
    start.go_to_start_page()
    start.go_to_shop()

    shop = ShopPage(driver)
    shop.go_to_product_killenium_butcher()

    kb = KillenniumButcher(driver)
    kb.go_to_cart()

    cp = CartPage(driver)
    cp.product_confirmation(product, price)

    checkout = CheckoutPage(driver)
    checkout.payment_with_positive_information(product, price)
