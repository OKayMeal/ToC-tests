from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from BaseHighScoreFormTest import BaseHighScoreFormTest
from pages.HighScoresPage import HighScoresPage
from pages.MainMenuPage import MainMenuPage
from pages.PlayPage import PlayPage
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
    
    
    def test_HSForm_0002(self):
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
        
    
    def test_HSForm_0003(self):
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
    
    
    def test_HSForm_0004(self):
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
    
    
    def test_HSForm_0005(self):
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
    
    
    def test_HSForm_0006(self):
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
    
    
    def test_HSForm_0007(self):
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
    
    
    def test_HSForm_0008(self):
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
    
    
    def test_HSForm_0009(self):
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
    
    
    def test_HSForm_0010(self, driver: WebDriver):
        """
        Description:
        Test submitting the form with correct  NAME
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type correct name
        3. Click SUBMIT
        4. Click CONTINUE
        5. Click PLAY
        6. Click HIGH SCORES
        
        Expected Result:
        3. - the form should get successfuly submitted OR there is a connection error
        4 . - should get redirected to MAIN MENU
        6. - if there was no connection error - there should be a new HIGH SCORE record displayed
        """
        
        # !! TEST ONLY FOR DEV ENV !!
        assert driver.game_env == 'dev', f'This test should only be executed on dev env. Env: {driver.game_env}'
        
        correct_name = 'Correct test Name'
        
        self.high_score_form.enter_name(correct_name)
        self.high_score_form.submit_btn.click_btn()
        
        expected_msgs = ['submitted successfully', 'Could not connect to the server']
        
        self.high_score_form.get_submission_result() 
        actual_msg = self.high_score_form.submit_result_msg.text
        
        found_expected_msg = False
        submission_successful = False
        if expected_msgs[0] in actual_msg:
            found_expected_msg = True
            submission_successful = True
            
        elif expected_msgs[1] in actual_msg:
            found_expected_msg = True
        
        assert found_expected_msg, f'Expected messages "{expected_msgs}". Actual message: {actual_msg}'
        
        self.high_score_form.continue_btn.click_btn()
        
        main_menu = MainMenuPage(driver, True)
        main_menu.play_btn.click_btn()
        
        play_page = PlayPage(driver)
        play_page.high_scores_btn.click_btn()
        
        high_scores_page = HighScoresPage(driver)
        high_scores_page.get_page_state_and_elements()
        
        if submission_successful:
            expected_states = ['connected_records', 'no_connection']
            assert (high_scores_page.state in expected_states), f"After successful submission expected high scores page states are '{expected_states}'. Actual state:  {high_scores_page.state}"
            
            if high_scores_page.state == 'connected_records':
                # get all records and check if the newly added one is there
                name_found = False
                for data_element in high_scores_page.high_scores_table_data_elements:
                    if correct_name in data_element.text:
                        name_found = True
                        break
                assert name_found, f'Newly created record not found among the displayed high scores records'
                
        else:
            # submission was unsuccessful
            expected_states = ['connected_records', 'no_connection', 'no_connection']
            assert (high_scores_page.state in expected_states), f"After unsuccessful submission expected high scores page states are '{expected_states}'. Actual state:  {high_scores_page.state}"
            
            if high_scores_page.state == 'connected_records':
                # get all records and check if the one we were trying to add is NOT there
                name_found = False
                for data_element in high_scores_page.high_scores_table_data_elements:
                    if correct_name in data_element.text:
                        name_found = True
                        break
                assert not name_found, f'The record that failed to submit was found among the displayed high scores records'
                # NOTE: THIS ASSERTION IS VALID ONLY ON DEV ENV WITH EMPTY DB, BECAUSE ON PROD IT IS PERFECTLY FINE TO SEE SEVERAL RECORDS WITH THE SAME NAME VALUE
    

    def test_HSForm_0011(self):
        """
        Description:
        Test submitting the form with containing invalid characters
        
        Test Steps:
        1. Go to HIGH SCORE submit form (by making player die)
        2. In NAME field type icorrect name containing of invalid chars e.g. <, ' =
        3. Click SUBMIT
        
        Expected Result:
        3. - error should appear prompting user to type another name
        """
        invalid_name = "<script>alert()</script>"
        
        self.high_score_form.enter_name(invalid_name)
    
        self.high_score_form.submit_btn.click_btn()
        
        expected_msg = 'try another name'
        self.high_score_form.get_form_warning()
        actual_msg = self.high_score_form.warning.text
        assert expected_msg in actual_msg, f'Expected message for invalid chars in NAME: {expected_msg}. Actual message: {actual_msg}'
        
        