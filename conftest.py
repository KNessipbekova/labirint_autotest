import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


@pytest.fixture()
def browser(request):
    path = '/Users/kundyzns/Downloads/chromedriver-mac-x64/Google Chrome for Testing'
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()