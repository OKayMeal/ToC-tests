from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import INTRO_DIV_LOC

class IntroPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.intro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INTRO_DIV_LOC))
    
    def skip_intro(self, first_prompt, second_prompt):
        """
        Skips the intro.

        Params:
        first_prompt (str): The method of prompting for the first action to skip. Should be 'keyboard' or 'mouse'.
        second_prompt (str): The method of prompting for the second action to skip. Should be 'keyboard' or 'mouse'.
        """

        possible_options = {
            'mouse': self.intro.click,
            'keyboard': lambda: self.press_key('Enter')
        }
        
        if first_prompt not in possible_options.keys() or second_prompt not in possible_options.keys():
            raise ValueError('Unsupported parameters. Possible options: "keyboard" or "mouse"')
        
        # perform actions
        possible_options[first_prompt]()
        possible_options[second_prompt]()
        