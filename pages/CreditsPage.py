from selenium.webdriver.remote.webdriver import WebDriver
from locators.locators import BTN_TEXT_LOCATORS, CREDITS_DIV_LOC, CREDITS_PARAGRAPHS_LOC
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Button import Button


class CreditsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # elements
        self.credits_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CREDITS_DIV_LOC))
        self.credits_paragraphs = self.credits_div.find_elements(*CREDITS_PARAGRAPHS_LOC)
        self.back_btn = Button(driver, BTN_TEXT_LOCATORS['back'])

    def count_word_occurences(self, word: str) -> int:
        """
        Checks the number of occurences of a given word in credits paragraphs.
        """

        word_occurences = 0
        for paragraph in self.credits_paragraphs:
            if word in paragraph.text:
                word_occurences += 1
        
        return word_occurences
