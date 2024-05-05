from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from pages.Button import Button
from locators.locators import BTN_TEXT_LOCATORS, NAME_INPUT_LOC, NAME_WARNING_LOC, SUBMISSION_RESULT_MSG_LOC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HighScoreFormPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
        # elements
        self.name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NAME_INPUT_LOC))
        self.submit_btn = Button(driver, BTN_TEXT_LOCATORS['submit_high_score'])
        self.continue_no_submit_btn = Button(driver, BTN_TEXT_LOCATORS['continue_no_submit'])
    
    
    def enter_name(self, name: str):
        """Enters given name into NAME input field"""
        
        self.name_input.send_keys(name)
        
    
    def get_form_warning(self):
        """Proceeds to locate warning message about profanity in NAME field"""
        
        self.warning = self.driver.find_element(*NAME_WARNING_LOC)
    
    
    def get_submission_result(self):
        """Proceeds to locate submission result message and continue btn after submitting"""
        
        self.submit_result_msg = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(SUBMISSION_RESULT_MSG_LOC))
        self.continue_btn = Button(self.driver, BTN_TEXT_LOCATORS['continue'])
        
        