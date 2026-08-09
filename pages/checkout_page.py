from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    # ========================================================
    # CHECKOUT INFORMATION
    # ========================================================

    FIRST_NAME = (By.ID, "first-name")

    LAST_NAME = (By.ID, "last-name")

    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    CANCEL_BUTTON = (By.ID, "cancel")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # ========================================================
    # CHECKOUT OVERVIEW
    # ========================================================

    FINISH_BUTTON = (By.ID, "finish")

    SUMMARY_TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    # ========================================================
    # ORDER CONFIRMATION
    # ========================================================

    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    COMPLETE_TEXT = (By.CSS_SELECTOR, ".complete-text")

    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)

    # ========================================================
    # ENTER FIRST NAME
    # ========================================================

    def enter_first_name(self, first_name):

        element = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

        element.clear()
        element.send_keys(first_name)

    # ========================================================
    # ENTER LAST NAME
    # ========================================================

    def enter_last_name(self, last_name):

        element = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME))

        element.clear()
        element.send_keys(last_name)

    # ========================================================
    # ENTER POSTAL CODE
    # ========================================================

    def enter_postal_code(self, postal_code):

        element = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE))

        element.clear()
        element.send_keys(postal_code)

    # ========================================================
    # ENTER CHECKOUT INFORMATION
    # ========================================================

    def enter_checkout_information(self, first_name, last_name, postal_code):

        self.enter_first_name(first_name)

        self.enter_last_name(last_name)

        self.enter_postal_code(postal_code)

    # ========================================================
    # CONTINUE TO CHECKOUT OVERVIEW
    # ========================================================

    def click_continue(self):

        button = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )

        self.driver.execute_script("arguments[0].click();", button)

        # Wait until checkout overview is loaded.
        # We accept either the expected URL or the Finish button.
        self.wait.until(
            lambda driver: "checkout-step-two.html" in driver.current_url
            or len(driver.find_elements(*self.FINISH_BUTTON)) > 0
        )

    # ========================================================
    # CANCEL CHECKOUT
    # ========================================================

    def click_cancel(self):

        button = self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON))

        button.click()

    # ========================================================
    # GET ERROR MESSAGE
    # ========================================================

    def get_error_message(self):

        element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))

        return element.text

    # ========================================================
    # GET TOTAL
    # ========================================================

    def get_total(self):

        element = self.wait.until(EC.visibility_of_element_located(self.SUMMARY_TOTAL))

        return element.text

    # ========================================================
    # FINISH ORDER
    # ========================================================

    def click_finish(self):

        button = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))

        button.click()

        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))

    # ========================================================
    # GET CONFIRMATION MESSAGE
    # ========================================================

    def get_confirmation_message(self):

        element = self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )

        return element.text

    # ========================================================
    # GET CONFIRMATION TEXT
    # ========================================================

    def get_confirmation_text(self):

        element = self.wait.until(EC.visibility_of_element_located(self.COMPLETE_TEXT))

        return element.text

    # ========================================================
    # BACK TO PRODUCTS
    # ========================================================

    def back_to_products(self):

        button = self.wait.until(EC.element_to_be_clickable(self.BACK_HOME_BUTTON))

        button.click()
        self.wait.until(EC.url_contains("inventory.html"))
