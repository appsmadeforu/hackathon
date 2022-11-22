from tests.base_test import BaseTest


class TestStickyNav(BaseTest):

    def test_sticky_main(self):
        try:
            self.driver.get(
                "https://andreidbr.github.io/JS30/24StickyNav/index.html#")
            print(self.driver.title)
            if self.driver.find_element_by_id("main"):
                print("Success")
 
            assert self.driver.find_element_by_id("main")
        except Exception as e:
            print(e)
        
 
    # false positive case - not found message
    def test_nav_on_scroll(self):
        try:
            self.driver.get(
                "https://andreidbr.github.io/JS30/24StickyNav/index.html#")
                                                                                                    
            if self.driver.find_element_by_xpath("//div[@class = 'logo' and style = 'padding-top: 0px']"):
            # if self.driver.find_element_by_css_selector("p.logo"):
                print("Successfully find ")
 
        except Exception as e:
            print(e)
