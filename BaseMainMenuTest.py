import pytest
from BaseTest import BaseTest
from pages.MainMenuPage import MainMenuPage

class BaseMainMenuTest(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_menu = MainMenuPage(driver, True)