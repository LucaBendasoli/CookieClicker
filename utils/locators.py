"""Module used for storing all locators used in the automation."""

from selenium.webdriver.common.by import By

# Dictionary that contains locators for the Cookie Clicker game
LOCATORS = {
    'accept_cookies' : (By.XPATH, '//a[contains(text(), "Got it!")]'),    # Accept website cookies
    'select_portuguese' : (By.XPATH , '//div[@id="langSelect-PT-BR"]'),   # Select portuguese
    'big_cookie' : (By.XPATH, '//button[@id="bigCookie"]'),               # Big cookie button
    'buildings' : (By.XPATH, '//div[@class="product unlocked enabled"]'), # Buildings to buy
    'cookie_balance' : (By.XPATH, '//div[@id="cookies"]'),                # Cookie balance
    'upgrade' : (By.XPATH, '//div[@class="crate upgrade enabled"]')       # Upgrades to buy
}
