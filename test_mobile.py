from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from BaseMobileTest import BaseMobileTest
from pages.PauseMenu import PauseMenu

class TestMobile(BaseMobileTest):
    def test_Mobile_0001(self):
        """
        Description:
        Testing basic touch mobile controls after starting a new game

        Test Steps:
        1. Start the game with mobile screen size
        2. Do some basic movement around with mobile touch buttons

        Expected Result:
        2. player moves around with touch arrow keys. Ult touch btn shoots ULT
        """
        initial_coordinates = self.game.get_player_properties('coordinates')
        initial_ultReady = self.game.get_player_properties('ultReady')
        
        delays = [1, 0.5, 0.75, 1]
        i = 0
        for movement_btn in self.mobile_controls.movement_btns:
            # various delays are needed because player can end up in the same position
            # after walking for e.g. 1 second in each direction
            self.mobile_controls.send_touch_event(movement_btn)
            sleep(delays[i])
            self.mobile_controls.send_touch_event(movement_btn, 'touchend')
            i += 1
        
        self.mobile_controls.send_touch_event(self.mobile_controls.ult_btn)

        new_coordinates = self.game.get_player_properties('coordinates')
        new_ultReady = self.game.get_player_properties('ultimateReady')

        assert initial_coordinates != new_coordinates, f'Mobile movement failure - coordinates havent changed, initial: {str(initial_coordinates[0])}, {str(initial_coordinates[1])} - new: {str(new_coordinates[0])}, {str(new_coordinates[1])}' # type: ignore
        assert new_ultReady == False, f'ultimateReady state should be false after touching ult btn, initial: {str(initial_ultReady)} new: {str(new_ultReady)}'

    def test_Mobile_0002(self, driver: WebDriver):
        """
        Description:
        Testing Pause Menu button If it displays the Pause Menu correctly

        Test Steps:
        1. Start the game with mobile screen size
        2. Tap on Menu button on HUD 

        Expected Result:
        2. Pause Menu should display
        """
        self.hud.settings_btn.click()

        pause_menu = PauseMenu(driver)

        assert pause_menu.pause_menu_div.is_displayed(), "Pause menu not displayed"