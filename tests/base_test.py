from utils.aws_client import aws_client
from selenium import webdriver


def teardown_method(driver):
    return driver.quit()


def setup_driver(desired_capabilities=None):
    client_url = aws_client()
    return webdriver.Remote(client_url,
                            desired_capabilities or webdriver.DesiredCapabilities.FIREFOX)


class BaseTest:
    driver = setup_driver()
