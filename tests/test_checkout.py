import pytest

from pages.login_page import LoginPage
from pages.products_page_test import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.config import BASE_URL, USERNAME, PASSWORD


@pytest.fixture
def checkout_page(driver):

    # Login
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(USERNAME, PASSWORD)

    # Add product
    products_page = ProductsPage(driver)

    products_page.add_product_by_name("Sauce Labs Backpack")

    # Open cart
    products_page.open_cart()

    cart_page = CartPage(driver)

    # Checkout
    cart_page.click_checkout()

    return driver, CheckoutPage(driver)


@pytest.mark.regression
def test_checkout_information_page(checkout_page):

    driver, checkout = checkout_page

    assert "/checkout-step-one.html" in driver.current_url


@pytest.mark.regression
def test_enter_checkout_information(checkout_page):

    driver, checkout = checkout_page

    checkout.enter_checkout_information("Nirguna", "Valvekar", "500001")

    checkout.click_continue()

    assert "/checkout-step-two.html" in driver.current_url


@pytest.mark.regression
def test_checkout_total_displayed(checkout_page):

    driver, checkout = checkout_page

    checkout.enter_checkout_information("Nirguna", "Valvekar", "500001")

    checkout.click_continue()

    total = checkout.get_total()

    assert "Total:" in total
    assert "$" in total


@pytest.mark.regression
def test_complete_order(checkout_page):

    driver, checkout = checkout_page

    checkout.enter_checkout_information("Nirguna", "Valvekar", "500001")

    checkout.click_continue()

    checkout.click_finish()

    message = checkout.get_confirmation_message()

    assert message == "Thank you for your order!"


@pytest.mark.regression
def test_confirmation_page(checkout_page):

    driver, checkout = checkout_page

    checkout.enter_checkout_information("Nirguna", "Valvekar", "500001")

    checkout.click_continue()

    checkout.click_finish()

    assert "/checkout-complete.html" in driver.current_url

    message = checkout.get_confirmation_text()

    assert "Your order has been dispatched" in message
