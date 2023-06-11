import allure


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening home page")
    def open(self):
        self.driver.open()

    @allure.step("Getting the page title")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Getting the page URL")
    def get_page_url(self):
        return self.driver.current_url
