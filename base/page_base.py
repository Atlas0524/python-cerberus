import allure


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening home page")
    def open(self):
        self.driver.open()