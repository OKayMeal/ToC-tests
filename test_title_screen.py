from selenium.webdriver.remote.webdriver import WebDriver
from BaseTest import BaseTest
from pages.TitlePage import TitlePage

class TestTitleScreen(BaseTest):
    def test_TS_0001(self, driver: WebDriver, gameenv: str):
        """
        Description:
        Checking If launching the app with certain screen size initializes the game in mobile mode

        Test Steps:
        1. Initialize screen in mobile screen size
        2. Go to Title Screen

        Expected Result:
        TAP TO START should appear on the screen meaning the game initialized in mobile mode
        """
        driver.set_window_size(397, 813)
        driver.refresh()

        title_screen = TitlePage(driver)

        expected_text = "TAP TO START"
        actual_text = title_screen.pressEnterButton.text
        assert  actual_text == expected_text, f"Expected text: {expected_text}. Actual text: {actual_text}"
    
    def test_TS_0002(self, driver: WebDriver):
        """
        Description:
        Checking If launching the app with max screen size initializes the game in desktop mode

        Test Steps:
        1. Initialize screen in max screen size
        2. Go to Title Screen

        Expected Result:
        PRESS ENTER TO START should appear on the screen meaning the game initialized in desktop mode
        """
        driver.maximize_window()

        title_screen = TitlePage(driver)

        expected_text = "PRESS ENTER TO START"
        actual_text = title_screen.pressEnterButton.text
        assert  actual_text == expected_text, f"Expected text: {expected_text}. Actual text: {actual_text}"