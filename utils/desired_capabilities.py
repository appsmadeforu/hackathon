class DesiredCapabilities(object):

    FIREFOX = {
        "browserName": "firefox",
        "marionette": True,
        "acceptInsecureCerts": True,
        "platform": "ANY",
        "javascriptEnabled": True,
    }
    INTERNETEXPLORER = {
        "browserName": "internet explorer",
        "version": "",
        "platform": "WINDOWS",
        "javascriptEnabled": True,
    }
    CHROME = {
        "browserName": "chrome",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
    }
