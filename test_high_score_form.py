from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from BaseHighScoreFormTest import BaseHighScoreFormTest
from pages.TitlePage import TitlePage


class TestHighScoreForm(BaseHighScoreFormTest):
    def test_HSForm_0001(self, driver: WebDriver):
        """
        Description:
        Test proceeding to main menu without submitting high score

        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. Click CONTINUE WITHOUT SUBMITTING button

        Expected Result:
        2. - should get redirected to TITLE page
        """
        
        self.high_score_form.continue_no_submit_btn.click_btn()
        
        title_page = TitlePage(driver)
        
        assert title_page.pressEnterButton.is_displayed(), f'Not redirected to TITLE page after proceeding via CONTINUE WITHOUT SUBMITTING btn from HighScoreForm'
    
    
    def test_HSForm_0002(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with NAME  too long >30 chars

        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field try typing a name longer than 30 chars

        Expected Result:
        2. - the field should not allow user to type a name >30 chars
        """
        name_longer_than_30_chars = 'n4m3l0ng3Rth4n30ch4rs should not be allowed'
        
        self.high_score_form.enter_name(name_longer_than_30_chars)
        
        expected_input_value = name_longer_than_30_chars[:30]
        
        assert expected_input_value == self.high_score_form.name_input.get_attribute('value'), f"Expected value in NAME input field: {expected_input_value}. Actual value: {self.high_score_form.name_input.get_attribute('value')}"
        
    
    def test_HSForm_0003(self, driver: WebDriver):
        """
        Description:
        Test submitting the form WITH polish profanity with polish chars as NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type polish profanity with polish chars
        3. Click SUBMIT HIGHSCORE button

        Expected Result:
        3. - error should appear prompting user to type another name
        """
        
        name_profanity_with_polish_chars = 'pierdolę cię'
        
        self.high_score_form.enter_name(name_profanity_with_polish_chars)
        
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for polish profanity in NAME: {expected_msg}. Actual message: {actual_msg}'
    
    
    def test_HSForm_0004(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with polish profanity WITHOUT polish chars as NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type polish profanity without polish chars                                                        
        3. Click SUBMIT HIGHSCORE button
        
        Expected Result:
        3. - error should appear prompting user to type another name
        """
        
        name_profanity_without_polish_chars = 'pieprzniety kurwidolek'
        
        self.high_score_form.enter_name(name_profanity_without_polish_chars)
        
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for polish profanity in NAME: {expected_msg}. Actual message: {actual_msg}'
    
    
    def test_HSForm_0005(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with polish profanity mixed upper/lower cases as NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type polish profanity with mixed upper/lower cases                                                                                                         
        3. Click SUBMIT HIGHSCORE button
        
        Expected Result:
        3. - error should appear prompting user to type another name
        """
        
        name_profanity_mixed_upper_lower = 'WkUrwIonA dUpA'
        
        self.high_score_form.enter_name(name_profanity_mixed_upper_lower)
        
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for polish profanity in NAME: {expected_msg}. Actual message: {actual_msg}'
    
    
    def test_HSForm_0006(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with polish profanity as a sub-string as NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type polish profanity as substring                                                                                                  
        3. Click SUBMIT HIGHSCORE button
        
        Expected Result:
        3. - error should appear prompting user to type another name
        """
        
        name_profanity_substring = 'Imie i nagleChujowaWstawka'
        
        self.high_score_form.enter_name(name_profanity_substring)
    
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for polish profanity in NAME: {expected_msg}. Actual message: {actual_msg}'
    
    
    def test_HSForm_0007(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with english profanity as NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type english profanity
        3. Click SUBMIT
        
        Expected Result:
        3. - error should appear prompting user to type another name
        """
        
        name_profanity = 'asshole'
        
        self.high_score_form.enter_name(name_profanity)
    
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for english profanity in NAME: {expected_msg}. Actual message: {actual_msg}'
    
    
    def test_HSForm_0008(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with english profanity mixed upper/lower case as NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type english profanity mixed upper/lower cases
        3. Click SUBMIT
        
        Expected Result:
        3. - error should appear prompting user to type another name
        """
        
        name_profanity_mixed_upper_lower = 'soN oF a BiTch'
        
        self.high_score_form.enter_name(name_profanity_mixed_upper_lower)
    
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for english profanity in NAME: {expected_msg}. Actual message: {actual_msg}'
    
    
    def test_HSForm_0009(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with english profanity as sub-string  as NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type english profanity as substring
        3. Click SUBMIT
        
        Expected Result:
        3. - error should appear prompting user to type another name
        """
        
        name_profanity_substring = 'JohnFuCksPrettyCUntS'
        
        self.high_score_form.enter_name(name_profanity_substring)
    
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for english profanity in NAME: {expected_msg}. Actual message: {actual_msg}'