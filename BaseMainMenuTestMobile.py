import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from BaseTest import BaseTest
from pages.MainMenuPage import MainMenuPage

class BaseMainMenuTestMobile(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        driver.set_window_size(397, 813)
        self.main_menu = MainMenuPage(driver, True, True)