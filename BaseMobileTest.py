from time import sleep
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from BaseTest import BaseTest
from pages.MainMenuPage import MainMenuPage
from pages.PlayPage import PlayPage
from pages.IntroPage import IntroPage
from pages.Game import Game
from pages.GameHUD import GameHUD
from pages.MobileControls import MobileControls

class BaseMobileTest(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        driver.set_window_size(397, 813)
        driver.refresh()
        main_menu = MainMenuPage(driver, True, True)

        main_menu.play_btn.click_btn()
        
        play_page = PlayPage(driver)
        play_page.main_game_btn.click_btn()
        
        intro = IntroPage(driver)
        intro.skip_intro('mouse', 'mouse')
        
        self.game = Game(driver)
        sleep(2) # ensure the game is loaded
        self.hud = GameHUD(driver)
        self.mobile_controls = MobileControls(driver)
