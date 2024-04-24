from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from BaseHighScoreFormTest import BaseHighScoreFormTest


class TestHighScoreForm(BaseHighScoreFormTest):
    def test_HSForm_0001(self, driver: WebDriver):
        sleep(3)