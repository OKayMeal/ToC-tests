from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from pages.Button import Button
from locators.locators import BTN_TEXT_LOCATORS, END_GAME_STATS_DIV_LOC, END_GAME_STATS_LOC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EndGameScreenPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
        # elements
        self.stats_wrapper = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(END_GAME_STATS_DIV_LOC))
        self.stats = driver.find_elements(*END_GAME_STATS_LOC)
        self.continue_btn = Button(driver, BTN_TEXT_LOCATORS['continue'])
        