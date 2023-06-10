import allure

from base.page_base import PageBase
from locators.locators import InventoryPageLocators


class InventoryPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting the page title")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Adding item to cart")
    def add_item_to_cart(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Getting the number of inventory items")
    def get_number_of_inventory_items(self):
        return int(self.driver.find_element(*InventoryPageLocators.shopping_cart_badge).text)
