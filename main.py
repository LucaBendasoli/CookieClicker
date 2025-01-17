"""
    For now this file is only here for testing and will be modified throughout the project.
    When everything is ready, this file will load the main execution logic of the project,
    instance of the created classes and the call of their functions
"""

from utils.CookieClickerDriver import CookieClickerDriver

cookieDriver = CookieClickerDriver()
cookieDriver.open_url()
cookieDriver.select_language()

while True:
    cookieDriver.click_big_cookie()
    cookieDriver.look_for_buildings_to_buy()