from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def press_key(self, key: str):
        """
        Presses a given keyboard key
        """

        if key == 'ENTER' or key == 'Enter':
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        else:
            actions = ActionChains(self.driver)
            actions.key_down(key)
            actions.perform()
            sleep(1)
            actions.key_up(key)
            actions.perform()
        