from selenium.webdriver.common.by import By


class LogInPageLocators:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    login_logo = (By.CLASS_NAME, "login_logo")
    error_username_required_box = (By.CSS_SELECTOR, '[data-test="error"]')
    error_password_required_box = (By.CSS_SELECTOR, '[data-test="error"]')
    error_close_button = (By.CLASS_NAME, "error-button")


class InventoryPageLocators:
    add_sauce_labs_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
