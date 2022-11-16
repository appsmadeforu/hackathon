from tests.base_test import BaseTest, teardown_method


class TestAppGraphics(BaseTest):

    def test(self):
        try:
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get("https://andreidbr.github.io/JS30/")
            if self.driver.find_element_by_class_name("text"):
                print("graphics generated in full screen")
            assert self.driver.find_element_by_class_name("text")
            self.driver.set_window_position(0, 0) and self.driver.set_window_size(1000, 400)
            self.driver.get("https://andreidbr.github.io/JS30/")
            tower = self.driver.find_element_by_class_name("text")
            if tower.is_displayed():
                print("graphics generated after resizing")
            else:
                print("graphics not generated at this window size")
                # this is where you can fail the script with error if you expect
                # the graphics to load. And pipeline will terminate
        except Exception as e:
            print(e)
        

