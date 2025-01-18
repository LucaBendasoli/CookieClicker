from selenium.webdriver.common.by import By

LOCATORS = {
    'select_portuguese' : (By.XPATH , '//div[@id="langSelect-PT-BR"]'), 
    'big_cookie' : (By.XPATH, '//button[@id="bigCookie"]'),
    'buildings' : (By.XPATH, '//div[@class="product unlocked enabled"]'),
    'cookie_balance' : (By.XPATH, '//div[@id="cookies"]'),
    'upgrade' : (By.XPATH, '//div[@class="crate upgrade enabled"]')
}