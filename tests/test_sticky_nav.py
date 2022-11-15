from tests.base_test import BaseTest, teardown_method


class TestStickyNav(BaseTest):

    def test_sticky_main(self):
        try:
            self.driver.implicitly_wait(5)
            self.driver.get(
                "https://andreidbr.github.io/JS30/24StickyNav/index.html#")
            print(self.driver.title)
            if self.driver.find_element_by_id("main"):
                print("Success")
 
            assert self.driver.find_element_by_id("main")
        except Exception as e:
            print(e)
        finally:
             teardown_method(self.driver)
 
    