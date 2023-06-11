import allure
import pytest

from pages.swag_labs.login_page import LoginPage
from test_data.test_data import SwagLabPasswords
from test_data.test_data import SwagLabUsers
from test_data.test_data import SwagLabsDefaults


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    @allure.title("Login page")
    @allure.description("Verify the Swag Labs page title is correct")
    def test_login_page_title(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        assert (SwagLabsDefaults.DEFAULT_SWAG_LABS_TITLE in login_page.get_page_title())

    @allure.title("Login page")
    @allure.description("Verify a standard user is able to login to Swag Labs")
    def test_standard_user_can_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(SwagLabUsers.standard_user, SwagLabPasswords.password)
        assert (SwagLabsDefaults.DEFAULT_LOGGED_IN_URL in login_page.get_page_url())

    @allure.title("Login page")
    @allure.description("Verify a locked-out user is unable to login to Swag Labs")
    def test_locked_out_user_can_not_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(SwagLabUsers.locked_out_user, SwagLabPasswords.password)
        assert (SwagLabsDefaults.DEFAULT_LOGGED_IN_URL not in login_page.get_page_url())
        assert (SwagLabsDefaults.DEFAULT_LOCKED_OUT_LOGIN_ERROR_MESSAGE in login_page.get_login_error_message())
