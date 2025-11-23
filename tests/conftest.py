import pytest
from selenium import webdriver

browser = [
    "Firefox",
    "Chrome"
]

@pytest.fixture(params=browser)
def driver(request):
    driver = getDriver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()


def getDriver(browser):
    if browser == 'Firefox':
        return webdriver.Firefox()
    elif browser == 'Chrome':
        return webdriver.Chrome()