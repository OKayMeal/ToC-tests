from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import GAME_CANVAS_LOC

class Game(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # elements
        self.game_canvas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(GAME_CANVAS_LOC))
        self.game_state = None
          
    def set_player_properties(self, property: str, value: int | str | list):
        """
        Executes JS script to set given property to player object
        """
        
        self.driver.execute_script(f'window.player.{property} = {value};')
    
        
    def get_player_properties(self, property: str):
        """
        Executes JS script to retrieve given property from custom window property window.player

        Available properties:
        'coordinates' - returns [player.x, player.y]
        any other viable property of player object e.g. ultimateReady, equipment, hp, etc.
        """

        if (property == 'coordinates'):
            return self.driver.execute_script('return [window.player.x, window.player.y];')
        else:
            return self.driver.execute_script(f'return window.player.{property};')


    def get_game_state(self):
        """
        Executes JS script to retrieve custom window property window.gameState.
        """
        
        return self.driver.execute_script('return window.gameState;')