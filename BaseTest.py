import pytest
from pages.MainMenuPage import MainMenuPage
from collections import Counter

class BaseTest():
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_menu = MainMenuPage(driver, True)
    
    
    def are_lists_equal(self, list1: list, list2: list):
        return Counter(list1) == Counter(list2)
