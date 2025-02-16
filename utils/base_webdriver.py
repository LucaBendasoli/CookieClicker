"""THE CLASS IN THIS MODULE SOULDN'T BE INSTANTIATED DIRECTLY, INSTEAD,
IT SHOULD BE INHERITED BY A CLASS THAT IMPLEMENTS THE URL ATTRIBUTE."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

class WebDriver:
    """Abstract class that facilitates the usage
    of selenium webdriver functionalities."""

    def __init__(self):
        """Initializes the WebDriver instance with a Chrome driver."""
        self._driver = webdriver.Chrome()

    def open_url(self) -> None:
        """Opens the url of the driver instance that inherits this class."""
        self._driver.get(self.url)

    def click_webelement(self,
        locator: str,
        timeout:int = 10,
        condition = EC.element_to_be_clickable
    ) -> None:
        """Wait for a web element to be clickable and clicks it.
        If not found, raises an exception."""
        WebDriverWait(self._driver, timeout).until(condition(locator)).click()

    def find_webelement(self,
        locator: str,
        timeout: int = 10,
        condition = EC.presence_of_element_located
    ) -> WebElement|list[WebElement]:
        """Wait for a (or many) web element in the page to be located and
        returns it (or them) if found. If not found, raises an exception."""
        if timeout == 0:
            return self._driver.find_element(*locator)
        return WebDriverWait(self._driver, timeout).until(condition(locator))
