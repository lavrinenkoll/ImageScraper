from selenium.webdriver.support.ui import WebDriverWait


class ModelParser:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.links = []