
import allure
import logging
from allure_commons.types import AttachmentType

from tests.base_test import BaseTest


logger = logging.getLogger(__name__)


class SeleniumWrappers(BaseTest):

    def open_application_site(self, url):
        self.driver.get(url)
        return self

    def get_page_title(self):
        return self.driver.title

    def clear_element_text(self, element_id):
        self.get_element(element_id).clear()
        logger.info("Text field" + element_id + "is cleared ")
        return self

    def input_element_text(self, input_text, element_id, element_type="id", ):
        element = self.get_element(element_id=element_id, element_type=element_type)
        element.clear()
        element.send_keys(input_text)

    def click_button(self, element_id, element_type="id", element_index=0):
        element = self.get_element(element_id=element_id, element_type=element_type)
        element.click()
        return 0

    def click_link(self, element_id):
        self.get_element(element_id).click()
        return self

    def close_all_browsers(self):
        self.driver.quit()
        return self

    def close_window(self):
        self.driver.close()
        return self

    def maximize_browser_window(self):
        return self.driver.maximize_window()

    def assert_two_values(self, actual_text, expected_text):

        actual_text = str(actual_text)
        expected_text = str(expected_text)

        try:
            assert actual_text == expected_text
            logger.info("Validation PASSED: Actual: {} and Expected: {}".format(actual_text,
                                                                                expected_text))
        except AssertionError:
            logger.error("Validation FAILED: Actual: {} and Expected: {}".format(actual_text,
                                                                                 expected_text))
            allure.attach(name='Screenshot {}',
                          body=self.driver.get_screenshot_as_png(),
                          attachment_type=AttachmentType.PNG)
            raise AssertionError("Please see screenshot")
                
        return actual_text == expected_text

    def get_driver_function(self, element_type="id"):
        driver = self.driver
        if element_type == "class":
            driver_function = driver.find_elements_by_class_name
        elif element_type == "id":
            driver_function = driver.find_elements_by_id
        elif element_type == "xpath":
            driver_function = driver.find_elements_by_xpath
        else:
            assert False
        return driver_function

    def get_element(self, element_id, element_type="id", element_index=0):
        driver_function = self.get_driver_function(element_type=element_type)
        try:
            element = driver_function(element_id)[element_index]
        except IndexError:
            logger.error("Cannot find element - Type: %s, Name: %s",
                         element_type, element_id)
            return
        return element

    def select_checkbox_byflag(self, isflag, element_id, element_type="id"):
        # Select checkbox based on the isflag - True (Select) /False (unselect)
        if isflag:
            self.select_checkbox(element_id, element_type="id")  # check checkbox if it is not checked
        else:
            self.unselect_checkbox(element_id, element_type="id")  # uncheck checkbox

        return self

    def select_checkbox(self, element_id, element_type="id"):
        logger.info("Selecting checkbox '%s'." % element_id)
        element = self.get_element(element_id=element_id, element_type=element_type)
        element.click()

    def unselect_checkbox(self, element_id, element_type="id"):
        # Removes selection of checkbox identified by `locator`.

        logger.info("Un-selecting checkbox '%s'." % element_id)
        element = self.get_element(element_id=element_id, element_type=element_type)
        if element.is_selected():
            element.click()
        return self

    def select_radio_button(self, element_id, element_type="id"):
        logger.info("Selecting checkbox '%s'." % element_id)
        element = self.get_element(element_id=element_id, element_type=element_type)
        element.click()
