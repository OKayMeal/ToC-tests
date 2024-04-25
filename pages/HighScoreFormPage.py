from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from pages.Button import Button
from locators.locators import BTN_TEXT_LOCATORS, NAME_INPUT_LOC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HighScoreFormPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
        # elements
        self.name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NAME_INPUT_LOC))
        self.submit_btn = Button(driver, BTN_TEXT_LOCATORS['submit_high_score'])
        self.continue_no_submit_btn = Button(driver, BTN_TEXT_LOCATORS['continue_no_submit'])