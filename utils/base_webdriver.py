"""THE CLASS IN THIS MODULE SOULDN'T BE INSTANTIATED DIRECTLY, INSTEAD,
IT SHOULD BE INHERITED BY A CLASS THAT IMPLEMENTS THE URL ATTRIBUTE."""

#TODO: Implement abstract class functionality to avoid instantiation of this class.

from selenium import webdriver
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
        """Wait a specific time (timeout parameter) for a web element
        to be clickable and clicks it. If no elements are found, it
        raises an exception.

        Args:
            locator (str): The locator of the element to be clicked.
            timeout (int): The time in seconds to wait for the element to be clickable.
            condition (function): The expected condition choosed for the WebDriverWait function
        """
        WebDriverWait(self._driver, timeout).until(condition(locator)).click()

    def find_webelement(self,
        locator: str,
        timeout: int = 10,
        condition = EC.presence_of_element_located
    ) -> WebElement|list[WebElement]:
        """Wait a specific time (timeout parameter) for a web element
        in the page to be located and returns it if found.
        If no elements are found, an exception is raised.

        Args:
            locator (str): The locator of the element to be found.
            timeout (int): The time in seconds to wait for the element to be found.
            condition (function): The expected condition choosed for the WebDriverWait function."""
        if timeout == 0:
            return self._driver.find_element(*locator)
        return WebDriverWait(self._driver, timeout).until(condition(locator))
