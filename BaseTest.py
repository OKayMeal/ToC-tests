import pytest
from pages.MainMenuPage import MainMenuPage

class BaseTest():
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_menu = MainMenuPage(driver, True)
