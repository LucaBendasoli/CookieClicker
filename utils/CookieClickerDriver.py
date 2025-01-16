from .locators import LOCATORS
from .BaseWebDriver import WebDriver

class CookieClickerDriver(WebDriver):

    def __init__(self):
        super().__init__()
        self.url = 'https://orteil.dashnet.org/cookieclicker/'

    def select_language(self) -> None:
        
        """Selects the language in the game"""
        
        self.click_webelement(LOCATORS['select_portuguese'])

    def click_big_cookie(self) -> None:
        
        """Clicks the big cookie in the game"""
        
        self.click_webelement(LOCATORS['big_cookie'])