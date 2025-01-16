from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class WebDriver:

    def __init__(self):
        
        """Initializes the WebDriver instance with a Chrome driver."""
        
        self._driver = webdriver.Chrome()

    def open_url(self) -> None:
        
        """Opens the url of the driver instance"""
        
        self._driver.get(self.url)

    def click_webelement(self, locator: str, timeout:int = 10, condition = EC.element_to_be_clickable) -> None:
        
        """Clicks on a web element in the page"""
        
        WebDriverWait(self._driver, timeout).until(condition(locator)).click()
        