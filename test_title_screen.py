from selenium.webdriver.remote.webdriver import WebDriver
from BaseTest import BaseTest
from pages.TitlePage import TitlePage

class TestTitleScreen(BaseTest):
    def test_TS_0001(self, driver: WebDriver):
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
    
    def test_TS_0003(self, driver: WebDriver):
        """
        Description:
        Checking if launching the app in mobile mode forces the browser window to go fullscreen

        Test Steps:
        1. Initialize screen in mobile screen size
        2. Go to Title Screen 3.
        Tap on “Tap to Start”

        Expected Result:
        The browser window should enter fullscreen mode
        """
        driver.set_window_size(397, 813)
        driver.refresh()

        title_screen = TitlePage(driver)
        window_size_before_full_screen = driver.get_window_size()

        # clicking on the button should enter the full screen browser mode
        title_screen.pressEnterButton.click()

        screen_width = driver.execute_script("return screen.width")
        screen_height = driver.execute_script("return screen.height")
        assert window_size_before_full_screen['width'] < screen_width and window_size_before_full_screen['height'] < screen_height
