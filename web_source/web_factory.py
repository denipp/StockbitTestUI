from selenium import webdriver
from web_source.Test import Test

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
optionsFirefox = webdriver.FirefoxOptions()
optionsFirefox.add_argument("--disable-infobars")
optionsFirefox.add_argument("start-maximized")
optionsFirefox.add_argument("--disable-extensions")

def get_web(browser):

    if browser == "chrome":
        return Test(webdriver.Chrome(options=options))