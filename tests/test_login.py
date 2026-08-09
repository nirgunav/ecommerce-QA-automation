import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.login_page import LoginPage

from utils.config import BASE_URL, USERNAME, PASSWORD


@pytest.mark.login
@pytest.mark.smoke
def test_valid_login(driver):

    # Open application
    driver.get(BASE_URL)

    # Create page object
    login_page = LoginPage(driver)

    # Login
    login_page.login(USERNAME, PASSWORD)

    # Verify successful login
    assert login_page.get_page_title() == "Products"


@pytest.mark.login
def test_invalid_username(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login("invalid_user", PASSWORD)

    error = login_page.get_error_message()

    assert "Username and password do not match" in error


@pytest.mark.login
def test_invalid_password(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(USERNAME, "wrong_password")

    error = login_page.get_error_message()

    assert "Username and password do not match" in error


@pytest.mark.login
def test_empty_username(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_password(PASSWORD)

    login_page.click_login()

    error = login_page.get_error_message()

    assert "Username is required" in error


@pytest.mark.login
def test_empty_password(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(USERNAME)

    login_page.click_login()

    error = login_page.get_error_message()

    assert "Password is required" in error
