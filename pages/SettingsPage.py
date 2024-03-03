from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import BTN_TEXT_LOCATORS, SETTINGS_DIV_LOC, SETTINGS_FIELDS_GENERIC_LOC
from pages.Button import Button

class SettingsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # elements
        self.settings_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SETTINGS_DIV_LOC))
        self.settings_fields = self.settings_div.find_elements(*SETTINGS_FIELDS_GENERIC_LOC)
        self.controls_btn = Button(driver, BTN_TEXT_LOCATORS['controls'])
        self.apply_btn = Button(driver, BTN_TEXT_LOCATORS['apply'])
        self.back_btn = Button(driver, BTN_TEXT_LOCATORS['back'])

    def make_changes_in_settings(self) -> list[bool]:
        """
        Makes changes in settings. The changes are just clicking each setting field.
        """
        changed_settings: list[bool] = []

        for setting_field in self.settings_fields:
            setting_field.click()
            changed_settings.append(setting_field.is_selected())

        return changed_settings
    
    def check_settings_saved(self, changed_settings: list[bool]) -> bool:
        """
        Checks whether the settings got properly saved by comparing current settings with the ones set before
        @param changed_settings - settings that were applied before
        """

        current_settings: list[bool] = []

        for setting_field in self.settings_fields:
            current_settings.append(setting_field.is_selected())
        
        return current_settings == changed_settings
    
    def leave_without_clicking_apply(self, save_changes: bool):
        """
        Navigates back without having clicked APPLY button.
        @param save_changes - whether to save changes or not
        """

        self.back_btn.click_btn()

        yes_btn = Button(self.driver, BTN_TEXT_LOCATORS['yes'])
        no_btn = Button(self.driver, BTN_TEXT_LOCATORS['no'])

        if save_changes:
            yes_btn.click_btn()
        else:
            no_btn.click_btn()
