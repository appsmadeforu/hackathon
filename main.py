# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tests.test_app_graphics import TestAppGraphics
from tests.test_sticky_nav import TestStickyNav

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_graphics = TestAppGraphics()
    test_graphics.test()

    test_sticky = TestStickyNav()
    test_sticky.test_sticky_main()
    test_sticky.test_nav_on_scroll()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
