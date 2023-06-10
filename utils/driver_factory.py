from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from extensions.webdriver_extended import WebDriverExtended
from webdriver_listener.webdriver_listener import WebDriverListener


class DriverFactory:
    SUPPORTED_BROWSERS = ["chrome", "firefox"]

    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            driver = WebDriverExtended(
                webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options),
                WebDriverListener(), config
            )
            return driver
        raise Exception("Provide a valid driver name: " + str(DriverFactory.SUPPORTED_BROWSERS))
