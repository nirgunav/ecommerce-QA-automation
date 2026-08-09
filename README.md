# E-Commerce QA Automation Framework

A Selenium-based test automation framework built with Python and Pytest for validating an e-commerce web application. The framework follows the Page Object Model (POM) design pattern and covers the complete shopping workflow from login to order completion.

## 🚀 Project Overview

This project automates functional and regression testing for an e-commerce application.

The automated flow covers:

- User Login
- Product browsing
- Product selection
- Add to Cart
- Cart validation
- Checkout information
- Checkout overview
- Order completion
- Return to products

The project currently contains **21 automated test cases**, with all **21 tests passing successfully**.

## 🛠️ Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Chrome WebDriver
- HTML Test Reports
- Git & GitHub

## 📁 Project Structure

```text
ecommerce-QA-automation/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── products_page_test.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_google.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── screenshot.py
│
├── reports/
│   └── test_report.html
│
├── conftest.py
├── create_test_scenarios.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md