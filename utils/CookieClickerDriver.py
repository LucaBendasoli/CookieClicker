from ..config.locators import LOCATORS

class CookieClickerDriver(WebDriver):

    def __init__(self):
        super().__init__()
        self.url = 'https://orteil.dashnet.org/cookieclicker/'

    def select_language(self) -> None:
        self.click_webelement(LOCATORS['select_portuguese'])

    def click_big_cookie(self) -> None:
        self.click_webelement(LOCATORS['big_cookie'])