from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from locators.locators import BTN_TEXT_LOCATORS, NAVIGATION_WRAPPER_LOC
from pages.Button import Button
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlayPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # elements
        self.navigation_wrapper = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(NAVIGATION_WRAPPER_LOC))
        self.main_game_btn = Button(driver, BTN_TEXT_LOCATORS['main_game'])
        self.high_scores_btn = Button(driver, BTN_TEXT_LOCATORS['high_scores'])
        self.survival_btn = Button(driver, BTN_TEXT_LOCATORS['survival'])
        self.back_btn = Button(driver, BTN_TEXT_LOCATORS['back'])