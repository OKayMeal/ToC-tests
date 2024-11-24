import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from BaseTest import BaseTest
from pages.MainMenuPage import MainMenuPage

class BaseMainMenuTest(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, driver : WebDriver):
        driver.maximize_window()
        self.main_menu = MainMenuPage(driver, True)