from typing import Iterable
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
        
    def look_for_buildings_to_buy(self) -> None:
    
        """Looks for buildings to buy in the game"""
    
        cookie_balance = self.find_webelement(LOCATORS['cookie_balance'], 0.5).text
        cookie_balance = int(cookie_balance.split()[0].replace(',', ''))
        try:
            buildings = self.find_webelement(LOCATORS['buildings'], 0)
        except:
            return
        if not isinstance(buildings, Iterable):
            buildings.click()
            return
        buildings[0].click()