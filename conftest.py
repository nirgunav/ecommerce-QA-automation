import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config import BROWSER, IMPLICIT_WAIT
from utils.screenshot import take_screenshot


@pytest.fixture
def driver(request):

    if BROWSER.lower() == "chrome":

        options = Options()

        # Start Chrome maximized
        options.add_argument("--start-maximized")

        # Disable Chrome password manager
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            },
        )

        # Disable browser notifications
        options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(options=options)

    else:

        raise ValueError(f"Unsupported browser: {BROWSER}")

    driver.implicitly_wait(IMPLICIT_WAIT)

    yield driver

    # ========================================================
    # TAKE SCREENSHOT WHEN TEST FAILS
    # ========================================================

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            take_screenshot(driver, request.node.name)

    driver.quit()


# ========================================================
# PYTEST REPORT HOOK
# ========================================================


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
