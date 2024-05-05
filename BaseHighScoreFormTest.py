from time import sleep
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from BaseTest import BaseTest
from pages.HighScoreFormPage import HighScoreFormPage
from pages.EndGameScreenPage import EndGameScreenPage
from pages.MainMenuPage import MainMenuPage
from pages.PlayPage import PlayPage
from pages.IntroPage import IntroPage
from pages.Game import Game

class BaseHighScoreFormTest(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, driver: WebDriver):
        main_menu = MainMenuPage(driver, True)
        main_menu.play_btn.click_btn()
        
        play_page = PlayPage(driver)
        play_page.main_game_btn.click_btn()
        
        intro = IntroPage(driver)
        intro.skip_intro('mouse', 'mouse')
        
        game = Game(driver)
        sleep(2) # ensure the game is loaded
        
        # kill the player
        game.set_player_properties('hp', 0)
        
        end_game_screen = EndGameScreenPage(driver)
        end_game_screen.continue_btn.click_btn()
        
        self.high_score_form = HighScoreFormPage(driver)