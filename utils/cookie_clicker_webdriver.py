"""Module that contains the webdriver class for Cookie Clicker game."""

from typing import Iterable
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import LOCATORS
from .base_webdriver import WebDriver

class CookieClickerDriver(WebDriver):
    """This class inherits the base webdriver class and implements methods that
    are specific to the Cookie Clicker game like clicking the big cookie, buying
    builds and upgrades."""

    def __init__(self):
        super().__init__()
        self.url = 'https://orteil.dashnet.org/cookieclicker/'

    def select_language(self) -> None:
        """Selects the language in the game"""
        self.click_webelement(LOCATORS['select_portuguese'])

    def accept_cookies(self) -> None:
        """Accepts all cookies from Cookie Clicker's website.\n
        ...funny isn't it? (〜￣▽￣)〜"""
        try:
            self.click_webelement(LOCATORS['accept_cookies'])
        except (NoSuchElementException, TimeoutException):
            pass

    def click_big_cookie(self) -> None:
        """Clicks the big cookie in the game"""
        self.click_webelement(LOCATORS['big_cookie'])

    def look_for_buildings_to_buy(self) -> None:
        """Looks for buildings to buy in the game"""
        try:
            buildings = self.find_webelement(LOCATORS['buildings'], 0)
        except (NoSuchElementException, TimeoutException):
            return
        if not isinstance(buildings, Iterable):
            buildings.click()
            return
        buildings[0].click()

    def look_for_upgrades_to_buy(self) -> None:
        """Looks for upgrades to buy in the game"""
        try:
            upgrade = self.find_webelement(LOCATORS['upgrade'], 0)
        except (NoSuchElementException, TimeoutException):
            return
        if not isinstance(upgrade, Iterable):
            upgrade.click()
            return
        upgrade[0].click()
