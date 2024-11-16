from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import SETTINGS_HUD_BTN_LOC
from pages.BasePage import BasePage

class GameHUD(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # elements
        self.settings_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SETTINGS_HUD_BTN_LOC))