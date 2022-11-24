
from pages.elemnentsPage import ElementsPage
import pytest


class TestElementsPage(ElementsPage):

    def test_title(self):
        try:
            self.open_application_site("https://ultimateqa.com/simple-html-elements-for-automation/")
            """
            ("https://demoqa.com/elements")
            """
            self.maximize_browser_window()
            self.check_page_title()
        except Exception as e:
            print(e)

    def test_text_boxes(self):
        try:
            self.verfiy_text_boxes()
        except Exception as e:
            print(e)

    def test_button(self):
        try:
            self.verify_button()
        except Exception as e:
            print(e)

    def test_check_box(self):
        try:
            self.verify_check_boxes()
        except Exception as e:
            print(e)

    def test_radio_button(self):
        try:
            self.verify_radio_button()
        except Exception as e:
            print(e)