from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriver:

    def __init__(self):
        self._driver = webdriver.Chrome()

    def open_url(self) -> None:
        self._driver.get(self.url)

    def click_webelement(self, locator: str, timeout:int = 10, condition = EC.element_to_be_clickable) -> None:
        WebDriverWait(self._driver, timeout).until(condition(locator)).click()
