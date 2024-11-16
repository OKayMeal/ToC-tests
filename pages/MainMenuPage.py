from selenium.webdriver.remote.webdriver import WebDriver
from locators.locators import BTN_TEXT_LOCATORS, VERSION_INDICATOR_LOC
from pages.BasePage import BasePage
from pages.Button import Button
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.PatchNotesPage import PatchNotesPage
from selenium.webdriver.common.alert import Alert
from pages.TitlePage import TitlePage


class MainMenuPage(BasePage):
    def __init__(self, driver: WebDriver, app_launch: bool = False, mobile: bool = False):
        super().__init__(driver)

        # navigate to main menu from title screen upon app_launch - this is just pressing ENTER key
        if app_launch:
            title_screen = TitlePage(driver)
            
            if mobile:
                title_screen.pressEnterButton.click()
            else:
                title_screen.press_key('ENTER')

        # elements
        self.play_btn = Button(self.driver, BTN_TEXT_LOCATORS['play'])
        self.cherem_pedia_btn = Button(self.driver, BTN_TEXT_LOCATORS['cherem_pedia'])
        self.settings_btn = Button(self.driver, BTN_TEXT_LOCATORS['settings'])
        self.credits_btn = Button(self.driver, BTN_TEXT_LOCATORS['credits'])
        self.exit_btn = Button(self.driver, BTN_TEXT_LOCATORS['exit'])
        self.version_div = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(VERSION_INDICATOR_LOC))
    
    def display_patch_notes(self):
        """
        Asserts version indicator div and clicks on it.   
        """

        # click on version div
        assert self.version_div.is_displayed(), 'version div not found'
        
        expected_version = self.version_div.find_element(by=By.TAG_NAME, value='p').text
        
        self.version_div.click()

        return PatchNotesPage(self.driver, expected_version)
    
    def exit_app(self):
        """
        Proceeds to exit the app by clicking on EXIT button.
        Returns the alert that should display upon exiting the app.
        """

        self.exit_btn.click_btn()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        return Alert(self.driver)