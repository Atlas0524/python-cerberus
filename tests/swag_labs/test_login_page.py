import allure
import pytest

from pages.swag_labs.login_page import LoginPage
from test_data.test_data import SwagLabPasswords
from test_data.test_data import SwagLabUsers

DEFAULT_SWAG_LABS_LOGO_NAME = "Swag Labs"


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    @allure.title("Login page")
    @allure.description("Verify Swag Labs logo is present and correct on Login page")
    def test_login_page_title(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        assert (DEFAULT_SWAG_LABS_LOGO_NAME in login_page.get_page_title())

    @allure.title("Login page")
    @allure.description("Verify a standard user is able to login to Swag Labs")
    def test_standard_user_can_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(SwagLabUsers.standard_user, SwagLabPasswords.password)
        assert (DEFAULT_SWAG_LABS_LOGO_NAME in login_page.get_page_title())
