import allure
import pytest

from locators.locators import InventoryPageLocators
from pages.swag_labs.inventory_page import InventoryPage
from pages.swag_labs.login_page import LoginPage
from test_data.test_data import SwagLabPasswords
from test_data.test_data import SwagLabUsers


@pytest.mark.usefixtures("setup")
class TestInventoryPage:
    @allure.title("Inventory page")
    @allure.description("Verify Swag Labs can add a backpack to the cart")
    def test_add_backpack_to_cart_is_successful(self):
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        login_page.open()
        login_page.login(SwagLabUsers.standard_user, SwagLabPasswords.password)
        inventory_page.add_item_to_cart(InventoryPageLocators.add_sauce_labs_backpack)
        number_of_items_in_cart = inventory_page.get_number_of_inventory_items()
        assert (number_of_items_in_cart == 1)
