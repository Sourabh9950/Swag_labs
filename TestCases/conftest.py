import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()

def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_option)

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/v1/")
    yield driver
    driver.quit()
