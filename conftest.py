import pytest
import time
from selenium import webdriver
from utils.aws_client import aws_client
from utils.desired_capabilities import DesiredCapabilities
import logging

def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='Browser to run tests'
    )

@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser

@pytest.fixture
def get_driver(request, get_browser):
    driver = None
    desired_capabilities = None
    if get_browser == 'chrome':
        desired_capabilities = DesiredCapabilities.CHROME
    elif get_browser == 'firefox':
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    elif get_browser == 'ie':
        desired_capabilities = DesiredCapabilities.INTERNETEXPLORER
    time.sleep(5)
    logger = logging()
    client_url = aws_client()
    driver = webdriver.Remote(client_url, desired_capabilities)
    request.cls.driver = driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()