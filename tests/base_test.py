from utils.aws_client import aws_client
from selenium import webdriver
import argparse
from utils.desired_capabilities import DesiredCapabilities


def teardown_method(driver):
    return driver.quit()


def setup_driver(desired_capabilities=None):
    client_url = aws_client()
    return webdriver.Remote(client_url, desired_capabilities)


class BaseTest:
    parser = argparse.ArgumentParser(
        description='Perform some basic selenium tests.')
    parser.add_argument('browser', choices=['chrome', 'firefox', 'ie'], nargs='?', default='chrome',
                        help='in which browser to test')
    args = parser.parse_args()
    if args.browser == 'chrome':
        caps = DesiredCapabilities.CHROME
    elif args.browser == 'firefox':
        caps = webdriver.DesiredCapabilities.FIREFOX
    elif args.browser == 'ie':
        caps = DesiredCapabilities.INTERNETEXPLORER

    driver = setup_driver(caps)
