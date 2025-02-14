"""
    Main file that orchestrates the whole process of playing the Cookie Clicker game.
"""

from utils.CookieClickerDriver import CookieClickerDriver

cookieDriver = CookieClickerDriver()
cookieDriver.open_url()
cookieDriver.select_language()

while True:
    cookieDriver.click_big_cookie()
    cookieDriver.look_for_upgrades_to_buy()
    cookieDriver.look_for_buildings_to_buy()