import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config import BROWSER, IMPLICIT_WAIT
from utils.screenshot import take_screenshot


@pytest.fixture
def driver(request):

    if BROWSER.lower() == "chrome":

        options = Options()

        options.add_argument("--start-maximized")

        # GitHub Actions / CI environment
        if os.getenv("GITHUB_ACTIONS") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    driver.implicitly_wait(IMPLICIT_WAIT)

    yield driver

    # Take screenshot when test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        take_screenshot(driver, request.node.name)

    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
