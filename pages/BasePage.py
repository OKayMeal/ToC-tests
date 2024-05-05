from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    
    
    def wait_for_loading_to_finish(self, locator: tuple):
        """Waits for loading to finish - meaning until the loader specified by 'locator' disappears"""
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(locator)
        )
        