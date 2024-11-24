from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import BTN_TEXT_LOCATORS, PAUSE_MENU_DIV_LOC
from pages.BasePage import BasePage
from pages.Button import Button

class PauseMenu(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # elements
        self.pause_menu_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PAUSE_MENU_DIV_LOC))
        self.resume_btn = Button(self.driver, BTN_TEXT_LOCATORS['resume'])
        self.settings_btn = Button(self.driver, BTN_TEXT_LOCATORS['settings'])
        self.cherem_pedia_btn = Button(self.driver, BTN_TEXT_LOCATORS['cherem_pedia'])
        self.restart_btn = Button(self.driver, BTN_TEXT_LOCATORS['restart'])
        self.exit_btn = Button(self.driver, BTN_TEXT_LOCATORS['exit'])
