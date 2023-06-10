# A Python UI Guardian worthy of Hades trust

The collection of tests contains:

- user login tests (correct / incorrect login and password)

## Project Structure

Here you can find a short description of main directories and it's content

- [locators](locators) - there are locators of web elements in locators.py grouped in classes
- [pages](pages) - there are sets of method for each test step
- [tests](tests) - there are sets of tests for main functionalities of website
- [reports](reports) - if you run tests with Allure, tests reports will be saved in this directory
- [utils](utils) - this directory contains files responsible for configuration, e.g. driver_factory.py for webdriver
  management

## Project Features

- framework follows page object pattern
- logger has been implemented in each step of test cases, e.g.

```
@allure.title("Login page")
@allure.description("Verify Swag Labs logo is present and correct on Login page")
def test_login_page_title(self):
    login_page = LoginPage(self.driver)
    login_page.open()
    assert (DEFAULT_SWAG_LABS_LOGO_NAME in login_page.get_page_title())
```

- Chrome and Firefox are preconfigured in DriverFactory class:

```
@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
```

## Getting Started

Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Run Automated Tests

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first

```
File > Settings > Tools > Python Integrated Tools > Testing
```

After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow.

## Generate Test Report

To generate all tests report using Allure you need to run tests by command first:

```
$ pytest --alluredir=<reports directory path>
```

After that you need to use command:

```
$ allure serve <reports directory path>
```