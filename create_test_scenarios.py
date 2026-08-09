from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

# ============================================================
# 1. CREATE WORKBOOK
# ============================================================

workbook = Workbook()

sheet = workbook.active
sheet.title = "Test Scenarios"


# ============================================================
# 2. HEADERS
# ============================================================

headers = ["Scenario ID", "Requirement ID", "Module", "Test Scenario", "Priority"]

sheet.append(headers)


# ============================================================
# 3. ALL TEST SCENARIOS
# ============================================================

scenarios = [
    # ========================================================
    # REGISTRATION - 10
    # ========================================================
    [
        "TS-REG-001",
        "REQ-REG-01",
        "Registration",
        "Verify that a new user can register with valid information",
        "High",
    ],
    [
        "TS-REG-002",
        "REQ-REG-02",
        "Registration",
        "Verify validation of mandatory registration fields",
        "High",
    ],
    [
        "TS-REG-003",
        "REQ-REG-03",
        "Registration",
        "Verify registration with a valid email format",
        "High",
    ],
    [
        "TS-REG-004",
        "REQ-REG-03",
        "Registration",
        "Verify registration with an invalid email format",
        "High",
    ],
    [
        "TS-REG-005",
        "REQ-REG-04",
        "Registration",
        "Verify registration with a password meeting password requirements",
        "High",
    ],
    [
        "TS-REG-006",
        "REQ-REG-04",
        "Registration",
        "Verify registration with a password that does not meet password requirements",
        "High",
    ],
    [
        "TS-REG-007",
        "REQ-REG-05",
        "Registration",
        "Verify registration using an already registered email address",
        "High",
    ],
    [
        "TS-REG-008",
        "REQ-REG-02",
        "Registration",
        "Verify registration with all mandatory fields empty",
        "High",
    ],
    [
        "TS-REG-009",
        "REQ-REG-02",
        "Registration",
        "Verify registration with partially completed mandatory fields",
        "Medium",
    ],
    [
        "TS-REG-010",
        "REQ-REG-01",
        "Registration",
        "Verify that the user receives confirmation after successful registration",
        "Medium",
    ],
    # ========================================================
    # LOGIN - 15
    # ========================================================
    [
        "TS-LOGIN-001",
        "REQ-LOGIN-01",
        "Login",
        "Verify that a user can log in with valid credentials",
        "High",
    ],
    [
        "TS-LOGIN-002",
        "REQ-LOGIN-02",
        "Login",
        "Verify login with an invalid username and valid password",
        "High",
    ],
    [
        "TS-LOGIN-003",
        "REQ-LOGIN-02",
        "Login",
        "Verify login with a valid username and invalid password",
        "High",
    ],
    [
        "TS-LOGIN-004",
        "REQ-LOGIN-02",
        "Login",
        "Verify login with both invalid username and invalid password",
        "High",
    ],
    [
        "TS-LOGIN-005",
        "REQ-LOGIN-03",
        "Login",
        "Verify login with an empty username",
        "High",
    ],
    [
        "TS-LOGIN-006",
        "REQ-LOGIN-03",
        "Login",
        "Verify login with an empty password",
        "High",
    ],
    [
        "TS-LOGIN-007",
        "REQ-LOGIN-03",
        "Login",
        "Verify login with both username and password empty",
        "High",
    ],
    [
        "TS-LOGIN-008",
        "REQ-LOGIN-02",
        "Login",
        "Verify login behavior when username is entered with leading or trailing spaces",
        "Medium",
    ],
    [
        "TS-LOGIN-009",
        "REQ-LOGIN-02",
        "Login",
        "Verify login behavior when password is entered with leading or trailing spaces",
        "Medium",
    ],
    [
        "TS-LOGIN-010",
        "REQ-LOGIN-04",
        "Login",
        "Verify that an appropriate error message is displayed for invalid credentials",
        "High",
    ],
    [
        "TS-LOGIN-011",
        "REQ-LOGIN-01",
        "Login",
        "Verify that the password field masks the entered password",
        "Medium",
    ],
    [
        "TS-LOGIN-012",
        "REQ-LOGIN-01",
        "Login",
        "Verify that successful login redirects the user to the home page",
        "High",
    ],
    [
        "TS-LOGIN-013",
        "REQ-LOGIN-02",
        "Login",
        "Verify application behavior after multiple consecutive failed login attempts",
        "Medium",
    ],
    [
        "TS-LOGIN-014",
        "REQ-LOGIN-01",
        "Login",
        "Verify that an authenticated user session is maintained during navigation",
        "Medium",
    ],
    [
        "TS-LOGIN-015",
        "REQ-LOGIN-05",
        "Login",
        "Verify that protected pages cannot be accessed after logout without authentication",
        "High",
    ],
    # ========================================================
    # PRODUCT SEARCH - 10
    # ========================================================
    [
        "TS-SEARCH-001",
        "REQ-SEARCH-01",
        "Product Search",
        "Verify that the user can search for an existing product by exact product name",
        "High",
    ],
    [
        "TS-SEARCH-002",
        "REQ-SEARCH-01",
        "Product Search",
        "Verify that the user can search for a product using a partial product name",
        "High",
    ],
    [
        "TS-SEARCH-003",
        "REQ-SEARCH-02",
        "Product Search",
        "Verify that matching products are displayed for a valid search",
        "High",
    ],
    [
        "TS-SEARCH-004",
        "REQ-SEARCH-03",
        "Product Search",
        "Verify that an appropriate message is displayed when no products match the search",
        "High",
    ],
    [
        "TS-SEARCH-005",
        "REQ-SEARCH-04",
        "Product Search",
        "Verify application behavior when the search field is empty",
        "Medium",
    ],
    [
        "TS-SEARCH-006",
        "REQ-SEARCH-01",
        "Product Search",
        "Verify search behavior using different letter cases",
        "Medium",
    ],
    [
        "TS-SEARCH-007",
        "REQ-SEARCH-01",
        "Product Search",
        "Verify search behavior with leading and trailing spaces",
        "Medium",
    ],
    [
        "TS-SEARCH-008",
        "REQ-SEARCH-01",
        "Product Search",
        "Verify search behavior using special characters",
        "Medium",
    ],
    [
        "TS-SEARCH-009",
        "REQ-SEARCH-02",
        "Product Search",
        "Verify that search results contain only products matching the search criteria",
        "High",
    ],
    [
        "TS-SEARCH-010",
        "REQ-SEARCH-01",
        "Product Search",
        "Verify search behavior when the search text is longer than the supported input length",
        "Low",
    ],
    # ========================================================
    # FILTERING & SORTING - 10
    # ========================================================
    [
        "TS-FILTER-001",
        "REQ-FILTER-01",
        "Product Filtering",
        "Verify that products can be filtered by category",
        "High",
    ],
    [
        "TS-FILTER-002",
        "REQ-FILTER-01",
        "Product Filtering",
        "Verify that displayed products belong to the selected category",
        "High",
    ],
    [
        "TS-FILTER-003",
        "REQ-FILTER-01",
        "Product Filtering",
        "Verify that the user can change the selected category filter",
        "Medium",
    ],
    [
        "TS-FILTER-004",
        "REQ-FILTER-01",
        "Product Filtering",
        "Verify behavior when a category contains no available products",
        "Medium",
    ],
    [
        "TS-FILTER-005",
        "REQ-FILTER-01",
        "Product Filtering",
        "Verify that filters can be cleared and the complete product list is restored",
        "Medium",
    ],
    [
        "TS-FILTER-006",
        "REQ-FILTER-03",
        "Product Filtering",
        "Verify that search and category filtering work together correctly",
        "High",
    ],
    [
        "TS-FILTER-007",
        "REQ-FILTER-02",
        "Product Sorting",
        "Verify that products can be sorted according to the supported sorting option",
        "High",
    ],
    [
        "TS-FILTER-008",
        "REQ-FILTER-04",
        "Product Sorting",
        "Verify that products are displayed in the correct sorting order",
        "High",
    ],
    [
        "TS-FILTER-009",
        "REQ-FILTER-02",
        "Product Sorting",
        "Verify sorting products from lowest price to highest price",
        "High",
    ],
    [
        "TS-FILTER-010",
        "REQ-FILTER-02",
        "Product Sorting",
        "Verify sorting products from highest price to lowest price",
        "High",
    ],
    # ========================================================
    # PRODUCT DETAILS - 8
    # ========================================================
    [
        "TS-PROD-001",
        "REQ-PRODUCT-01",
        "Product Details",
        "Verify that the user can open the product details page",
        "High",
    ],
    [
        "TS-PROD-002",
        "REQ-PRODUCT-02",
        "Product Details",
        "Verify that the product details page displays the correct product name",
        "High",
    ],
    [
        "TS-PROD-003",
        "REQ-PRODUCT-03",
        "Product Details",
        "Verify that the product details page displays the correct product price",
        "High",
    ],
    [
        "TS-PROD-004",
        "REQ-PRODUCT-04",
        "Product Details",
        "Verify that the product details page displays the correct product description",
        "Medium",
    ],
    [
        "TS-PROD-005",
        "REQ-PRODUCT-05",
        "Product Details",
        "Verify that product availability status is displayed correctly",
        "High",
    ],
    [
        "TS-PROD-006",
        "REQ-PRODUCT-01",
        "Product Details",
        "Verify that the user can navigate back from product details to the product listing",
        "Medium",
    ],
    [
        "TS-PROD-007",
        "REQ-PRODUCT-01",
        "Product Details",
        "Verify that the correct product details are displayed when different products are selected",
        "High",
    ],
    [
        "TS-PROD-008",
        "REQ-PRODUCT-01",
        "Product Details",
        "Verify that an unavailable or invalid product does not display incorrect product information",
        "High",
    ],
    # ========================================================
    # SHOPPING CART - 12
    # ========================================================
    [
        "TS-CART-001",
        "REQ-CART-01",
        "Shopping Cart",
        "Verify that an available product can be added to the shopping cart",
        "High",
    ],
    [
        "TS-CART-002",
        "REQ-CART-02",
        "Shopping Cart",
        "Verify that the added product is displayed correctly in the cart",
        "High",
    ],
    [
        "TS-CART-003",
        "REQ-CART-03",
        "Shopping Cart",
        "Verify that the correct product price is displayed in the cart",
        "High",
    ],
    [
        "TS-CART-004",
        "REQ-CART-04",
        "Shopping Cart",
        "Verify that the user can increase the product quantity in the cart",
        "High",
    ],
    [
        "TS-CART-005",
        "REQ-CART-04",
        "Shopping Cart",
        "Verify that the user can decrease the product quantity in the cart",
        "High",
    ],
    [
        "TS-CART-006",
        "REQ-CART-05",
        "Shopping Cart",
        "Verify that the cart total is recalculated after changing product quantity",
        "High",
    ],
    [
        "TS-CART-007",
        "REQ-CART-06",
        "Shopping Cart",
        "Verify that the user can remove a product from the cart",
        "High",
    ],
    [
        "TS-CART-008",
        "REQ-CART-07",
        "Shopping Cart",
        "Verify that the cart total is recalculated after removing a product",
        "High",
    ],
    [
        "TS-CART-009",
        "REQ-CART-01",
        "Shopping Cart",
        "Verify that multiple different products can be added to the cart",
        "High",
    ],
    [
        "TS-CART-010",
        "REQ-CART-05",
        "Shopping Cart",
        "Verify that the total price is calculated correctly for multiple products",
        "High",
    ],
    [
        "TS-CART-011",
        "REQ-CART-04",
        "Shopping Cart",
        "Verify cart behavior when product quantity reaches the minimum allowed value",
        "Medium",
    ],
    [
        "TS-CART-012",
        "REQ-CART-04",
        "Shopping Cart",
        "Verify cart behavior when product quantity reaches the maximum allowed value",
        "Medium",
    ],
    # ========================================================
    # CHECKOUT - 12
    # ========================================================
    [
        "TS-CHECKOUT-001",
        "REQ-CHECKOUT-01",
        "Checkout",
        "Verify that the user can proceed from the cart to the checkout page",
        "High",
    ],
    [
        "TS-CHECKOUT-002",
        "REQ-CHECKOUT-02",
        "Checkout",
        "Verify that the checkout page displays the required customer information fields",
        "High",
    ],
    [
        "TS-CHECKOUT-003",
        "REQ-CHECKOUT-03",
        "Checkout",
        "Verify validation of mandatory checkout fields",
        "High",
    ],
    [
        "TS-CHECKOUT-004",
        "REQ-CHECKOUT-03",
        "Checkout",
        "Verify checkout behavior when all mandatory fields are empty",
        "High",
    ],
    [
        "TS-CHECKOUT-005",
        "REQ-CHECKOUT-03",
        "Checkout",
        "Verify checkout behavior when only some mandatory fields are completed",
        "High",
    ],
    [
        "TS-CHECKOUT-006",
        "REQ-CHECKOUT-02",
        "Checkout",
        "Verify checkout with valid customer information",
        "High",
    ],
    [
        "TS-CHECKOUT-007",
        "REQ-CHECKOUT-04",
        "Checkout",
        "Verify that the user can select a supported payment method",
        "High",
    ],
    [
        "TS-CHECKOUT-008",
        "REQ-CHECKOUT-04",
        "Checkout",
        "Verify validation when a required payment option is not selected",
        "High",
    ],
    [
        "TS-CHECKOUT-009",
        "REQ-CHECKOUT-05",
        "Checkout",
        "Verify that the user can place an order with valid checkout information",
        "High",
    ],
    [
        "TS-CHECKOUT-010",
        "REQ-CHECKOUT-06",
        "Checkout",
        "Verify that an order confirmation is displayed after successful order placement",
        "High",
    ],
    [
        "TS-CHECKOUT-011",
        "REQ-CHECKOUT-05",
        "Checkout",
        "Verify that the final order amount matches the cart total before order placement",
        "High",
    ],
    [
        "TS-CHECKOUT-012",
        "REQ-CHECKOUT-05",
        "Checkout",
        "Verify that an order cannot be placed when required checkout information is invalid",
        "High",
    ],
    # ========================================================
    # ORDERS - 8
    # ========================================================
    [
        "TS-ORDER-001",
        "REQ-ORDER-01",
        "Orders",
        "Verify that the user can view order history",
        "High",
    ],
    [
        "TS-ORDER-002",
        "REQ-ORDER-02",
        "Orders",
        "Verify that order history displays order details correctly",
        "High",
    ],
    [
        "TS-ORDER-003",
        "REQ-ORDER-03",
        "Orders",
        "Verify that the user can open an individual order",
        "High",
    ],
    [
        "TS-ORDER-004",
        "REQ-ORDER-04",
        "Orders",
        "Verify that ordered products are displayed correctly",
        "High",
    ],
    [
        "TS-ORDER-005",
        "REQ-ORDER-04",
        "Orders",
        "Verify that ordered product quantities are displayed correctly",
        "High",
    ],
    [
        "TS-ORDER-006",
        "REQ-ORDER-04",
        "Orders",
        "Verify that ordered product prices are displayed correctly",
        "High",
    ],
    [
        "TS-ORDER-007",
        "REQ-ORDER-04",
        "Orders",
        "Verify that the order total is calculated and displayed correctly",
        "High",
    ],
    [
        "TS-ORDER-008",
        "REQ-ORDER-01",
        "Orders",
        "Verify that a newly placed order appears in the user's order history",
        "High",
    ],
    # ========================================================
    # PROFILE - 6
    # ========================================================
    [
        "TS-PROFILE-001",
        "REQ-PROFILE-01",
        "User Profile",
        "Verify that an authenticated user can view profile information",
        "Medium",
    ],
    [
        "TS-PROFILE-002",
        "REQ-PROFILE-02",
        "User Profile",
        "Verify that the user can update supported profile information",
        "Medium",
    ],
    [
        "TS-PROFILE-003",
        "REQ-PROFILE-02",
        "User Profile",
        "Verify that updated profile information is saved correctly",
        "High",
    ],
    [
        "TS-PROFILE-004",
        "REQ-PROFILE-03",
        "User Profile",
        "Verify that the user can change the account password",
        "High",
    ],
    [
        "TS-PROFILE-005",
        "REQ-PROFILE-03",
        "User Profile",
        "Verify that an invalid password change is rejected",
        "High",
    ],
    [
        "TS-PROFILE-006",
        "REQ-PROFILE-03",
        "User Profile",
        "Verify that the new password can be used for subsequent login",
        "High",
    ],
    # ========================================================
    # LOGOUT & ACCESS CONTROL - 4
    # ========================================================
    [
        "TS-LOGOUT-001",
        "REQ-LOGOUT-01",
        "Logout",
        "Verify that an authenticated user can log out successfully",
        "High",
    ],
    [
        "TS-LOGOUT-002",
        "REQ-LOGOUT-02",
        "Logout",
        "Verify that protected pages cannot be accessed after logout",
        "High",
    ],
    [
        "TS-LOGOUT-003",
        "REQ-LOGOUT-02",
        "Logout",
        "Verify that browser back navigation does not expose protected content after logout",
        "High",
    ],
    [
        "TS-LOGOUT-004",
        "REQ-LOGOUT-02",
        "Logout",
        "Verify that an unauthenticated user is redirected to the login page when accessing a protected page",
        "High",
    ],
]


# ============================================================
# 4. ADD SCENARIOS TO EXCEL
# ============================================================

for scenario in scenarios:
    sheet.append(scenario)


# ============================================================
# 5. FORMAT HEADER
# ============================================================

for cell in sheet[1]:

    cell.font = Font(bold=True)

    cell.alignment = Alignment(horizontal="center", vertical="center")


# ============================================================
# 6. FORMAT ALL CELLS
# ============================================================

for row in sheet.iter_rows():

    for cell in row:

        cell.alignment = Alignment(vertical="top", wrap_text=True)


# ============================================================
# 7. COLUMN WIDTHS
# ============================================================

sheet.column_dimensions["A"].width = 20
sheet.column_dimensions["B"].width = 20
sheet.column_dimensions["C"].width = 22
sheet.column_dimensions["D"].width = 75
sheet.column_dimensions["E"].width = 15


# ============================================================
# 8. FREEZE HEADER
# ============================================================

sheet.freeze_panes = "A2"


# ============================================================
# 9. AUTO FILTER
# ============================================================

sheet.auto_filter.ref = sheet.dimensions


# ============================================================
# 10. SAVE FILE
# ============================================================

output_file = "manual-testing/test-scenarios.xlsx"

workbook.save(output_file)


# ============================================================
# 11. RESULT
# ============================================================

print("Test scenarios Excel file created successfully!")
print(f"Total scenarios created: {len(scenarios)}")
print(f"File location: {output_file}")
