import pytest

from pages.login_page import LoginPage
from pages.products_page_test import ProductsPage
from pages.cart_page import CartPage

from utils.config import BASE_URL, USERNAME, PASSWORD


@pytest.fixture
def logged_in_cart(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(USERNAME, PASSWORD)

    products_page = ProductsPage(driver)

    products_page.add_product_by_name("Sauce Labs Backpack")

    products_page.open_cart()

    return driver, CartPage(driver)


@pytest.mark.regression
def test_cart_contains_product(logged_in_cart):

    driver, cart_page = logged_in_cart

    assert cart_page.get_cart_item_count() == 1

    assert "Sauce Labs Backpack" in cart_page.get_product_names()


@pytest.mark.regression
def test_cart_product_price(logged_in_cart):

    driver, cart_page = logged_in_cart

    prices = cart_page.get_product_prices()

    assert len(prices) == 1

    assert prices[0].startswith("$")


@pytest.mark.regression
def test_cart_quantity(logged_in_cart):

    driver, cart_page = logged_in_cart

    quantities = cart_page.get_quantities()

    assert quantities == ["1"]


@pytest.mark.regression
def test_remove_product(logged_in_cart):

    driver, cart_page = logged_in_cart

    cart_page.remove_product("Sauce Labs Backpack")

    assert cart_page.get_cart_item_count() == 0


@pytest.mark.regression
def test_continue_shopping(logged_in_cart):

    driver, cart_page = logged_in_cart

    cart_page.continue_shopping()

    assert "/inventory.html" in driver.current_url
