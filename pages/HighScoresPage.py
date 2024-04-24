from selenium.webdriver.remote.webdriver import WebDriver
from locators.locators import BTN_TEXT_LOCATORS, HIGHSCORES_TABLE, HIGHSCORES_TABLE_HEADERS_LOC, LOADING_LOC, NO_CONNECTION_P_LOC, NO_HIGHSCORES_P_LOC
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Button import Button


class HighScoresPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # initial state
        self.state = 'loading'

        # elements
        self.loading = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOADING_LOC))
        self.back_btn = Button(driver, BTN_TEXT_LOCATORS['back'])
        
        
    def get_page_state_and_elements(self):
        """
        Waits for loading to finish and then proceeds to get the page state and elements
        """
        self.wait_for_loading_to_finish(LOADING_LOC)

        if self.is_no_connection_state():
            self.state = 'no_connection'
            
            # get elements
            self.no_connection_error = self.driver.find_element(*NO_CONNECTION_P_LOC)
            
        elif self.is_connected_no_records_state():
            self.state = 'connected_no_records'
            
            # get elements
            self.no_records_warning = self.driver.find_element(*NO_HIGHSCORES_P_LOC)
            
        elif self.is_connected_records_state():
            self.state = 'connected_records'
            
            # get elements
            self.high_scores_table = self.driver.find_element(*HIGHSCORES_TABLE)
            self.high_scores_table_headers_elements = self.high_scores_table.find_elements(*HIGHSCORES_TABLE_HEADERS_LOC)
            
            self.high_scores_table_headers = []
            for element in self.high_scores_table_headers_elements:
                self.high_scores_table_headers.append(element.text)
            
                      
    def is_no_connection_state(self):
        return len(self.driver.find_elements(*NO_CONNECTION_P_LOC)) > 0
        
        
    def is_connected_no_records_state(self):
        return len(self.driver.find_elements(*NO_HIGHSCORES_P_LOC)) > 0
        
        
    def is_connected_records_state(self):
        return len(self.driver.find_elements(*HIGHSCORES_TABLE)) > 0