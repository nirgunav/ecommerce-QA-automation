from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    # ========================================================
    # LOCATORS
    # ========================================================

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")

    QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")

    REMOVE_BUTTONS = (By.CSS_SELECTOR, ".cart_button")

    CHECKOUT_BUTTON = (By.ID, "checkout")

    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)

    # ========================================================
    # CART INFORMATION
    # ========================================================

    def get_cart_item_count(self):

        items = self.driver.find_elements(*self.CART_ITEMS)

        return len(items)

    def get_product_names(self):

        elements = self.driver.find_elements(*self.PRODUCT_NAMES)

        return [element.text for element in elements]

    def get_product_prices(self):

        elements = self.driver.find_elements(*self.PRODUCT_PRICES)

        return [element.text for element in elements]

    def get_quantities(self):

        elements = self.driver.find_elements(*self.QUANTITY)

        return [element.text for element in elements]

    # ========================================================
    # REMOVE PRODUCT
    # ========================================================

    def remove_product(self, product_name):

        items = self.driver.find_elements(*self.CART_ITEMS)

        for item in items:

            name = item.find_element(*self.PRODUCT_NAMES)

            if name.text == product_name:

                remove_button = item.find_element(*self.REMOVE_BUTTONS)

                self.driver.execute_script("arguments[0].click();", remove_button)

                return

        raise ValueError(f"Product not found in cart: {product_name}")

    # ========================================================
    # CHECKOUT
    # ========================================================

    def click_checkout(self):

        checkout_button = self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", checkout_button
        )

        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))

        self.driver.execute_script("arguments[0].click();", checkout_button)

        self.wait.until(EC.url_contains("checkout-step-one.html"))

    # ========================================================
    # CONTINUE SHOPPING
    # ========================================================

    def continue_shopping(self):

        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        )

        button.click()

        self.wait.until(EC.url_contains("inventory.html"))
