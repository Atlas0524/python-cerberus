import allure

from base.page_base import PageBase
from locators.locators import LogInPageLocators


class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Opening login page")
    def open_login_page(self):
        self.open()

    @allure.step("Setting username")
    def set_username(self, username):
        element = self.driver.find_element(*LogInPageLocators.username_input).send_keys(username)

    @allure.step("Setting password")
    def set_password(self, password):
        self.driver.find_element(*LogInPageLocators.password_input).send_keys(password)

    @allure.step("Clicking login button")
    def click_login_button(self):
        self.driver.find_element(*LogInPageLocators.login_button).click()

    @allure.step("Get login error message")
    def get_login_error_message(self):
        return self.driver.find_element(*LogInPageLocators.login_error_message_box).text

    @allure.step("Sets the username and password inputs and clicks the Login button")
    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
