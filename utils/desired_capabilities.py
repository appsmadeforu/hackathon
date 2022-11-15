
class DesiredCapabilities(object):
   
    FIREFOX = {
        "browserName": "firefox",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
        "marionette": False}
    INTERNETEXPLORER = {"browserName": "internet explorer",
                        "version": "",
                        "platform": "WINDOWS",
                        "javascriptEnabled": True}
    CHROME = {"browserName": "chrome",
              "version": "",
              "platform": "ANY",
              "javascriptEnabled": True}
