"""
    Main file that orchestrates the whole process of playing Cookie Clicker.
"""

from utils.cookie_clicker_webdriver import CookieClickerDriver

def start_cookie_clicker() -> CookieClickerDriver:
    """Starts the Cookie Clicker game, selects portuguese as
    the language and returns the driver object."""
    cookie_driver = CookieClickerDriver()
    cookie_driver.open_url()
    cookie_driver.select_language()
    cookie_driver.accept_cookies()
    return cookie_driver

def click_and_buy_forever(cookie_driver: CookieClickerDriver) -> None:
    """Run a infinite loop that clicks the big cookie and looks
    for upgrades and buildings to buy as soon as they are available."""
    while True:
        cookie_driver.click_big_cookie()
        cookie_driver.look_for_upgrades_to_buy()
        cookie_driver.look_for_buildings_to_buy()

def main() -> None:
    """Main function that starts the game and plays it forever."""
    cookie_driver = start_cookie_clicker()
    click_and_buy_forever(cookie_driver)

if __name__ == '__main__':
    main()
