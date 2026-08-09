from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # ========================================================
    # LOCATORS
    # ========================================================

    USERNAME_INPUT = (By.ID, "user-name")

    PASSWORD_INPUT = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    PRODUCTS_TITLE = (By.CSS_SELECTOR, ".title")

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)

    # ========================================================
    # PAGE ACTIONS
    # ========================================================

    def enter_username(self, username):

        element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))

        element.clear()

        element.send_keys(username)

    def enter_password(self, password):

        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))

        element.clear()

        element.send_keys(password)

    def click_login(self):

        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

    # ========================================================
    # VALIDATION METHODS
    # ========================================================

    def get_error_message(self):

        element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))

        return element.text

    def get_page_title(self):

        element = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_TITLE))

        return element.text

    def is_login_page_displayed(self):

        return self.driver.find_element(*self.USERNAME_INPUT).is_displayed()
