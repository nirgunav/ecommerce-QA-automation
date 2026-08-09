import pytest

from pages.login_page import LoginPage
from pages.products_page_test import ProductsPage

from utils.config import BASE_URL, USERNAME, PASSWORD


@pytest.fixture
def logged_in_products_page(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(USERNAME, PASSWORD)

    return driver, ProductsPage(driver)


@pytest.mark.regression
def test_products_page_title(logged_in_products_page):

    driver, products_page = logged_in_products_page

    assert products_page.get_page_title() == "Products"


@pytest.mark.regression
def test_product_count(logged_in_products_page):

    driver, products_page = logged_in_products_page

    assert products_page.get_product_count() == 6


@pytest.mark.regression
def test_product_names_available(logged_in_products_page):

    driver, products_page = logged_in_products_page

    names = products_page.get_product_names()

    assert len(names) == 6

    assert all(name.strip() for name in names)


@pytest.mark.regression
def test_product_prices_available(logged_in_products_page):

    driver, products_page = logged_in_products_page

    prices = products_page.get_product_prices()

    assert len(prices) == 6

    assert all(price.startswith("$") for price in prices)


@pytest.mark.regression
def test_add_product_to_cart(logged_in_products_page):

    driver, products_page = logged_in_products_page

    products_page.add_product_by_name("Sauce Labs Backpack")

    products_page.open_cart()

    assert "/cart.html" in driver.current_url
