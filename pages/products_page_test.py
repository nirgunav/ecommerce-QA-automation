from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    # ========================================================
    # LOCATORS
    # ========================================================

    PRODUCTS_TITLE = (By.CSS_SELECTOR, ".title")

    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")

    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".inventory_item button")

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)

    # ========================================================
    # VALIDATION
    # ========================================================

    def get_page_title(self):

        element = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_TITLE))

        return element.text

    def get_product_count(self):

        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_ITEMS)
        )

        return len(products)

    # ========================================================
    # PRODUCT INFORMATION
    # ========================================================

    def get_product_names(self):

        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )

        return [element.text for element in elements]

    def get_product_prices(self):

        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_PRICES)
        )

        return [element.text for element in elements]

    # ========================================================
    # ADD PRODUCT TO CART
    # ========================================================

    def add_product_by_name(self, product_name):

        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_ITEMS)
        )

        for product in products:

            name = product.find_element(*self.PRODUCT_NAMES)

            if name.text == product_name:

                button = product.find_element(*self.ADD_TO_CART_BUTTONS)

                button.click()

                return

        raise ValueError(f"Product not found: {product_name}")

    # ========================================================
    # CART
    # ========================================================

    def open_cart(self):

        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()
