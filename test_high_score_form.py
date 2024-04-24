from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from BaseTest import BaseTest
from pages.PlayPage import PlayPage
from pages.IntroPage import IntroPage
from pages.Game import Game


class TestHighScoreForm(BaseTest):
    def test_HSForm_0001(self, driver: WebDriver):
        self.main_menu.play_btn.click_btn()
        
        play_page = PlayPage(driver)
        play_page.main_game_btn.click_btn()
        
        intro = IntroPage(driver)
        intro.skip_intro('mouse', 'mouse')
        
        game = Game(driver)
        sleep(3) # ensure the game is loaded
        
        # kill player
        game.set_player_properties('hp', 0)
        
        sleep(3)