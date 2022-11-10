from aws_utils.aws_client import AWSClient
from selenium import webdriver


class TestAppGraphics:

    def test(self):
        client = AWSClient()
        driver = client.connect_to_devicefarm(webdriver.DesiredCapabilities.FIREFOX)
        try:
            driver.implicitly_wait(30)
            driver.maximize_window()
            driver.get("https://andreidbr.github.io/JS30/")
            if driver.find_element_by_class_name("text"):
                print("graphics generated in full screen")
            assert driver.find_element_by_class_name("text")
            driver.set_window_position(0, 0) and driver.set_window_size(1000, 400)
            driver.get("https://andreidbr.github.io/JS30/")
            tower = driver.find_element_by_class_name("text")
            if tower.is_displayed():
                print("graphics generated after resizing")
            else:
                print("graphics not generated at this window size")
                # this is where you can fail the script with error if you expect
                # the graphics to load. And pipeline will terminate
        except Exception as e:
            print(e)
        finally:
            driver.quit()
