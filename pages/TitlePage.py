from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from locators.locators import PRESS_ENTER_BTN_LOC


class TitlePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # elements
        self.pressEnterButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PRESS_ENTER_BTN_LOC))

        