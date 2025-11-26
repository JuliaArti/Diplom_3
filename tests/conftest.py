import pytest
from selenium import webdriver

browser = [
    "Firefox",
    "Chrome"
]

@pytest.fixture(params=browser)
def driver(request):
    if request.param == 'Firefox':
        driver = webdriver.Firefox()
    elif request.param == 'Chrome':
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()