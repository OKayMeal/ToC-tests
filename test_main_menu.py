from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from BaseMainMenuTest import BaseMainMenuTest
from locators.locators import CREDITS_DIV_LOC, NG_BUTTON_TOGGLED_LOC, PATCH_NOTES_DIV_LOC, SETTINGS_DIV_LOC
from pages.HighScoresPage import HighScoresPage
from pages.MainMenuPage import MainMenuPage
from pages.CreditsPage import CreditsPage
from pages.SettingsPage import SettingsPage
from pages.Game import Game
from pages.PlayPage import PlayPage
from pages.CheremPediaPage import CheremPediaPage
from pages.PediaPage import PediaPage
from pages.IntroPage import IntroPage

class TestMainMenu(BaseMainMenuTest):
    def test_MMenu_0001(self, driver: WebDriver):
        """
        Description:
        Checking if correct patch notes display upon clicking on game's version indicator

        Test Steps:
        1. Go to main menu
        2. Click on game version indicator
        3. Click on BACK button

        Expected Result:
        Appropriate patch notes should appear for the current version of the game
        """

        patch_notes_page = self.main_menu.display_patch_notes()
        sleep(1) # ensure the patchnotes .txt files loaded
        assert patch_notes_page.patch_notes_div.is_displayed(), 'patchnotes div not found'
        assert patch_notes_page.patch_notes_header.is_displayed(), 'patchnotes header not found'
        assert patch_notes_page.patch_notes_text.is_displayed(), 'patch notes text not found'

        assert patch_notes_page.version in patch_notes_page.patch_notes_header.text, f'Expected version {patch_notes_page.version} not found in patchnotes header'

        # test BACK navi
        patch_notes_page.back_btn.click_btn()
        assert len(driver.find_elements(*PATCH_NOTES_DIV_LOC)) == 0, 'Patchnotes found in DOM after clicking BACK btn'



    def test_MMenu_0002(self, driver: WebDriver):
        """
        Description:
        Checking if EXIT button quits the app

        Test Steps:
        1. Go to main menu
        2. Click on EXIT button
        3. Confirm the action by clicking on OK button in the alert pop up

        Expected Result:
        User is redirected to 'about:blank' page
        """

        alert = self.main_menu.exit_app()
        
        # check if the alert informs the user he is about to 'exit' the app
        assert 'exit' in alert.text, 'Alert text is missing keyword "exit"'

        alert.accept()
        
        assert driver.current_url == 'about:blank', 'Quitting App to blank page unsuccesful'



    def test_MMenu_0003(self, driver: WebDriver):
        """
        Description:
        Checking if CREDITS button navigates to credits section

        Test Steps:
        1. Go to main menu
        2. Click on CREDITS button
        3. Click on BACK button

        Expected Result:
        Credits section should appear. BACK navigates to main menu
        """

        self.main_menu.credits_btn.click_btn()

        credits_page = CreditsPage(driver)
        assert credits_page.credits_div.is_displayed(), 'Credits section did not display'
        assert len(credits_page.credits_paragraphs) > 0, 'Credits paragraphs not found'

        game_creator_name = 'Kamil'
        game_creator_name_occurences = credits_page.count_word_occurences(game_creator_name)
        assert game_creator_name_occurences > 0, f'{game_creator_name} not found in Credits section'
        
        # test BACK navi
        credits_page.back_btn.click_btn()
        assert len(driver.find_elements(*CREDITS_DIV_LOC)) == 0, 'Credits div found in DOM after clicking BACK btn'



    def test_MMenu_0004(self, driver: WebDriver):
        """
        Description:
        Checking if SETTINGS button navigates to settings section

        Test Steps:
        1. Go to main menu
        2. Click on SETTINGS button
        3. Click on BACK button                                                                                                                                                         

        Expected Result:
        Settings section should be displayed. BACK navigates to main menu
        """

        self.main_menu.settings_btn.click_btn()
        settings_page = SettingsPage(driver)
        assert settings_page.settings_div.is_displayed() and len(settings_page.settings_fields) > 0, 'Settings section and/or settings fields not found'

        # BACK navi
        settings_page.back_btn.click_btn()
        assert len(driver.find_elements(*SETTINGS_DIV_LOC)) == 0, 'Settings div found in DOM after clicking BACK btn'



    def test_MMenu_0005(self, driver: WebDriver):
        """
        Description:
        Testing changing settings in settings section and saving it via APPLY button

        Test Steps:
        1. Go to main menu
        2. Click on SETTINGS button
        3. Make changes in settings
        4. Save the changes by clicking on APPLY button
        5. Click on BACK button
        6. Click on SETTINGS button

        Expected Result:
        Changed settings should save properly and remain in saved state when navigating to main menu and then again to settings section
        """

        self.main_menu.settings_btn.click_btn()

        settings_page = SettingsPage(driver)

        changed_settings = settings_page.make_changes_in_settings()
        settings_page.apply_btn.click_btn()
        settings_page.back_btn.click_btn()
        
        main_menu = MainMenuPage(driver)
        main_menu.settings_btn.click_btn()

        settings_page = SettingsPage(driver)
        assert settings_page.check_settings_saved(changed_settings), 'Settings were not saved correctly via APPLY btn'



    def test_MMenu_0006(self, driver: WebDriver):
        """
        Description:
        Testing changing settings in settings section and leaving testing section and accepting to save changes

        Test Steps:
        1. Go to main menu
        2. Click on SETTINGS button
        3. Make changes in settings
        4. Click on BACK button
        5. Accept to apply new settings by clicking on YES button
        6. Click on SETTINGS button

        Expected Result:
        Changed settings should save properly and remain in saved state when navigating to main menu and then again to settings section
        """

        self.main_menu.settings_btn.click_btn()

        settings_page = SettingsPage(driver)

        changed_settings = settings_page.make_changes_in_settings()
        settings_page.leave_without_clicking_apply(True)

        main_menu = MainMenuPage(driver)
        main_menu.settings_btn.click_btn()

        settings_page = SettingsPage(driver)
        assert settings_page.check_settings_saved(changed_settings), 'Settings were not saved correctly'


    def test_MMenu_0007(self, driver: WebDriver):
        """
        Description:
        Testing changing settings in settings section and leaving testing section and rejecting to save changes

        Test Steps:
        1. Go to main menu
        2. Click on SETTINGS button
        3. Make changes in settings
        4. Click on BACK button
        5. Reject to apply new settings by clicking on NO button
        6. Click on SETTINGS button

        Expected Result:
        Changed settings should not be savedand remain in default state when navigating to main menu and then again to settings section
        """

        self.main_menu.settings_btn.click_btn()

        settings_page = SettingsPage(driver)

        changed_settings = settings_page.make_changes_in_settings()
        settings_page.leave_without_clicking_apply(False)
        
        main_menu = MainMenuPage(driver)
        main_menu.settings_btn.click_btn()
        
        settings_page = SettingsPage(driver)
        assert not settings_page.check_settings_saved(changed_settings), 'Settings were saved despite rejecting to save settings'



    def test_MMenu_0008(self, driver: WebDriver):
        """
        Description:
        Testing starting a new game via PLAY-> MAIN GAME plus navigation back and forth

        Test Steps:
        1. Go to main menu
        2. Click on PLAY button
        3. Click on BACK button
        4. Click on PLAY button
        5. Click on MAIN GAME button

        Expected Result:
        The game should start
        """

        self.main_menu.play_btn.click_btn()
        
        play_page = PlayPage(driver)
        assert play_page.navigation_wrapper.is_displayed(), 'navigation wrapper for PLAY section btns not found'
        
        play_page.back_btn.click_btn()
        
        main_menu = MainMenuPage(driver)
        main_menu.play_btn.click_btn()
        
        play_page = PlayPage(driver)
        play_page.main_game_btn.click_btn()

        intro = IntroPage(driver)
        assert intro.intro.is_displayed(), 'Intro section not found'

        intro.skip_intro('mouse', 'mouse')
        
        game = Game(driver)
        assert game.game_canvas.is_displayed(), 'Game canvas not found'

        sleep(3) # to ensure the game loads

        tries_count = 0
        while game.game_state == None or tries_count < 5:
            game.game_state = game.get_game_state()
            tries_count += 1
        
        assert game.game_state == 'playing', 'The game is not in the playing state.'



    def test_MMenu_0009(self, driver: WebDriver):
        """
        Description:
        Testing if BESTIARY displays bestiary plus checking correct navigation to and out of bestiary.

        Test Steps:
        1. Go to main menu 
        2. Click on CHEREMPEDIA button 
        3. Click on BESTIARY
        4. Click on BACK
        5. Click on BACK

        Expected Result:
        Bestiary should be displayed
        """

        self.main_menu.cherem_pedia_btn.click_btn()
        cherem_pedia = CheremPediaPage(driver)
        
        cherem_pedia.bestiary_btn.click_btn()
        bestiary = PediaPage(driver, 'BESTIARY')
        
        assert bestiary.records_card.is_displayed(), 'records-card div not found in DOM after clicking BESTIARY btn'
        assert len(bestiary.records_images) != 0, 'records images not found in Bestiary'
        assert bestiary.pedia_card.is_displayed(), 'pedia-card div not found in DOM after clicking BESTIARY btn'
        assert len(bestiary.pedia_card.find_elements(by=By.XPATH, value='//p[text()="----"]')) == 3, '3 paragraphs with dummy text "----" not found in pedia-card'
        
        bestiary.back_btn.click_btn()
        cherem_pedia = CheremPediaPage(driver)
        assert cherem_pedia.navigation_wrapper.is_displayed(), 'navigation wrapper not found in DOM after clicking BACK btn'
        
        cherem_pedia.back_btn.click_btn()
        main_menu = MainMenuPage(driver)
        assert main_menu.version_div.is_displayed(), 'Version div (mmenu) not found in DOM after clicking BACK btn'



    def test_MMenu_0010(self, driver: WebDriver):
        """
        Description:
        Testing if ITEMS displays items pedia plus checking correct navigation to and out of items pedia.

        Test Steps:
        1. Go to main menu 
        2. Click on CHEREMPEDIA button 
        3. Click on ITEMS
        4. Click on BACK
        5. Click on BACK

        Expected Result:
        Items pedia should be displayed
        """

        self.main_menu.cherem_pedia_btn.click_btn()
        cherem_pedia = CheremPediaPage(driver)
        
        cherem_pedia.items_btn.click_btn()
        items_pedia = PediaPage(driver, 'ITEMS')
        
        assert items_pedia.records_card.is_displayed(), 'records-card div not found in DOM after clicking ITEMS btn'
        assert len(items_pedia.records_images) != 0, 'records images not found in Items pedia'
        assert items_pedia.pedia_card.is_displayed(), 'pedia-card div not found in DOM after clicking ITEMS btn'
        assert len(items_pedia.pedia_card.find_elements(by=By.XPATH, value='//p[text()="----"]')) == 3, '3 paragraphs with dummy text "----" not found in pedia-card'
        
        items_pedia.back_btn.click_btn()
        cherem_pedia = CheremPediaPage(driver)
        assert cherem_pedia.navigation_wrapper.is_displayed(), 'navigation wrapper not found in DOM after clicking BACK btn'
        
        cherem_pedia.back_btn.click_btn()
        main_menu = MainMenuPage(driver)
        assert main_menu.version_div.is_displayed(), 'Version div (mmenu) not found in DOM after clicking BACK btn'



    def test_MMenu_0011(self, driver: WebDriver):
        """
        Description:
        Testing if switching selected version in PATCHNOTES section displays appropriate patchnotes
        and if going back to mm and to PATCHNOTES again displays current version patch notes.

        Test Steps:
        1. Go to main menu
        2. Click on game version indicator for example 1.3.0alpha
        3. Click on any version in VERSIONS: section
        4. Click on BACK
        5. Click on game version indicator for example 1.3.0alpha

        Expected Result:
        Appropriate patch notes should display. Going back and forth to PATCHNOTES section always displays current version patchnotes
        until chosen different version in VERSIONS: section
        """
        
        patch_notes_page = self.main_menu.display_patch_notes()
        sleep(1) # ensure the patchnotes .txt files loaded
        all_versions = patch_notes_page.get_all_versions()

        for version in all_versions:
            patch_notes_page.select_version(version)

            assert version in patch_notes_page.patch_notes_header.text, f'Selected version {version} not found in patchnotes header'
        
        patch_notes_page.back_btn.click_btn()

        main_menu = MainMenuPage(driver)

        patch_notes_page = main_menu.display_patch_notes()
        assert patch_notes_page.version in patch_notes_page.patch_notes_header.text, f'Current version {patch_notes_page.version} not found in patchnotes header upon navigating to PatchNotes'


    def test_MMenu_0012(self, driver: WebDriver):
        """
        Description:
        Testing BESTIARY if clicking on monster's portrait results in displaying appropriate monster info 

        Test Steps:
        1. Go to main menu
        2. Click on CHEREMPEDIA button
        3. Click on BESTIARY
        4. Click on monster's portrait

        Expected Result:
        Appropriate monster's info should be displayed
        """
        
        self.main_menu.cherem_pedia_btn.click_btn()
        cherem_pedia = CheremPediaPage(driver)
        
        cherem_pedia.bestiary_btn.click_btn()
        bestiary = PediaPage(driver, 'BESTIARY')

        all_records = bestiary.get_all_records_names()

        for record in all_records:
            bestiary.select_record(record)
            
            assert bestiary.pedia_record_name.text == record, f'Selected record name {record} does not equal displayed record name {bestiary.pedia_record_name.text}'
            assert bestiary.pedia_selected_record_image.get_attribute('alt') == record, f"Selected record image {record} does not equal displayed record image {bestiary.pedia_selected_record_image.get_attribute('alt')}"


    def test_MMenu_0013(self, driver: WebDriver):
        """
        Description:
        Testing ITEMS pedia if clicking on item's portrait results in displaying appropriate item info 

        Test Steps:
        1. Go to main menu
        2. Click on CHEREMPEDIA button
        3. Click on ITEMS
        4. Click on item's portrait

        Expected Result:
        Appropriate item's info should be displayed
        """

        self.main_menu.cherem_pedia_btn.click_btn()
        cherem_pedia = CheremPediaPage(driver)
        
        cherem_pedia.items_btn.click_btn()
        items_pedia = PediaPage(driver, 'ITEMS')

        all_records = items_pedia.get_all_records_names()

        for record in all_records:
            items_pedia.select_record(record)
            
            assert items_pedia.pedia_record_name.text == record, f'Selected record name {record} does not equal displayed record name {items_pedia.pedia_record_name.text}'
            assert items_pedia.pedia_selected_record_image.get_attribute('alt') == record, f"Selected record image {record} does not equal displayed record image {items_pedia.pedia_selected_record_image.get_attribute('alt')}"


    def test_MMenu_0014(self, driver: WebDriver):
        """
        Description:
        Testing NG+ btn functionality in BESTIARY if it correctly toggles NG+ version of monster info,
        and if switching to another portait disables NG+ btn for the next selected monster.

        Test Steps:
        1. Go to main menu
        2. Click on CHEREMPEDIA button
        3. Click on BESTIARY
        4. Click on monster's portrait
        5. Click NG+ btn
        6. Click on another monster's portrait

        Expected Result:
        5 - the NG+ monster stats info should be displayed 
        6 - after clicking another portrait, the ng+ should be disabled for this monster until clicked
        """

        self.main_menu.cherem_pedia_btn.click_btn()
        cherem_pedia = CheremPediaPage(driver)
        
        cherem_pedia.bestiary_btn.click_btn()
        bestiary = PediaPage(driver, 'BESTIARY')

        all_records = bestiary.get_all_records_names()

        for record in all_records:
            bestiary.select_record(record)

            ng_toggled = driver.find_elements(*NG_BUTTON_TOGGLED_LOC)

            assert len(ng_toggled) == 0, "NG+ button still pressed after selecting another monster"

            record_stats = bestiary.get_all_stats()

            bestiary.ng_btn.click_btn()

            record_stats_NG = bestiary.get_all_stats()

            assert record_stats != record_stats_NG, f"Record's NG+ stats not displayed after clicking NG+ btn"


    def test_MMenu_0015(self, driver: WebDriver):
        """
        Description:
        Testing basic keyboard movement after starting a new game

        Test Steps:
        1. Go to main menu
        2. Click on PLAY button
        3. Click on MAIN GAME button
        4. Click on the screen twice to skip the intro story
        5. Do some basic movement around with keyboard keys W,S,A,D

        Expected Result:
        5. - player moves around with W,S,A,D keys. Q key shoots ULT
        """

        self.main_menu.play_btn.click_btn()
        
        play_page = PlayPage(driver)

        play_page.main_game_btn.click_btn()

        intro_page = IntroPage(driver)

        intro_page.skip_intro('mouse', 'mouse')

        game = Game(driver)
        sleep(3)
        initial_coordinates = game.get_player_properties('coordinates')
        initial_ultReady = game.get_player_properties('ultReady')
        sleep(1)

        movement_keys = ['w', 's', 'a', 'd']
        for movement_key in movement_keys:
            game.press_key(movement_key)
        
        game.press_key('q') # ult key
        
        new_coordinates = game.get_player_properties('coordinates')
        new_ultReady = game.get_player_properties('ultimateReady')

        assert initial_coordinates != new_coordinates, f'Keyboard movement failure - coordinates havent changed, initial: {str(initial_coordinates[0])}, {str(initial_coordinates[1])} - new: {str(new_coordinates[0])}, {str(new_coordinates[1])}' # type: ignore
        assert initial_ultReady != new_ultReady, f'ultimateReady state should be false after pressing Q ult keyboard key, initial: {str(initial_ultReady)} new: {str(new_ultReady)}'

    
    def test_MMenu_0016(self, driver: WebDriver):
        """
        Description:
        Testing HIGH SCORES section

        Test Steps:
        1. Go to main menu
        2. Click on PLAY button
        3. Click on HIGH SCORES button
        4. Click BACK
        5. Click BACK

        Expected Result:
        3. first it should display LOADING, then either "Could not connect to the servrer..." OR "There are no high scores yet" OR display the table of high scores.
        """
        
        self.main_menu.play_btn.click_btn()
        play_page = PlayPage(driver)
        
        play_page.high_scores_btn.click_btn()
        highscores_page = HighScoresPage(driver)
        
        assert highscores_page.loading.is_displayed(), "Loading element was not displayed"
        
        highscores_page.get_page_state_and_elements()
        
        if highscores_page.state == 'no_connection':
            eror_text = 'Could not connect'
            assert eror_text in highscores_page.no_connection_error.text, f"'{eror_text}' not found in {highscores_page.state}"
            
        elif highscores_page.state == 'connected_no_records':
            eror_text = 'no high scores submitted'
            assert eror_text in highscores_page.no_records_warning.text, f"'{eror_text}' not found in {highscores_page.state}"
        
        elif highscores_page.state == 'connected_records':
            expected_table_headers = [
                'NAME', 'LEVEL', 'TIME PLAYED', 'ENEMIES KILLED',
                'BOSSES DEFEATED', 'GOLD LOOTED', 'EQUIPMENT',
                'GOLD', 'DATE',
            ]
            actual_table_headers = highscores_page.high_scores_table_headers
            
            assert self.are_lists_equal(expected_table_headers, actual_table_headers), f"Expected High Scores table headers: {expected_table_headers}. Actual headers: {actual_table_headers}"
        
        # testing back navi
        highscores_page.back_btn.click_btn()
        play_page = PlayPage(driver)
        assert play_page.navigation_wrapper.is_displayed(), 'navigation wrapper for PLAY section btns not found after clicking BACK btn in HighScoresPage'
        
        play_page.back_btn.click_btn()
        main_menu = MainMenuPage(driver)
        assert main_menu.version_div.is_displayed(), 'Version div (mmenu) not found in DOM after clicking BACK btn in PlayPage'
         