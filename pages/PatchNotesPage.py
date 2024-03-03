from selenium.webdriver.remote.webdriver import WebDriver
from locators.locators import BTN_TEXT_LOCATORS, PATCH_NOTES_DIV_LOC, PATCH_NOTES_HEADER_LOC, PATCH_NOTES_TEXT_LOC, PATCH_NOTES_VERSIONS_INDICATORS_LOC, PATCH_NOTES_VERSIONS_LOC
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.Button import Button


class PatchNotesPage(BasePage):
    def __init__(self, driver: WebDriver, expected_version: str):
        super().__init__(driver)
        self.version = expected_version 

        # elements
        self.patch_notes_div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PATCH_NOTES_DIV_LOC))
        self.patch_notes_header = driver.find_element(*PATCH_NOTES_HEADER_LOC)
        self.patch_notes_text = driver.find_element(*PATCH_NOTES_TEXT_LOC)
        self.patch_notes_versions = driver.find_element(*PATCH_NOTES_VERSIONS_LOC)
        self.patch_notes_versions_indicators = self.patch_notes_versions.find_elements(*PATCH_NOTES_VERSIONS_INDICATORS_LOC)
        self.back_btn = Button(driver, BTN_TEXT_LOCATORS['back'])
    
    def select_version(self, version: str):
        selected_version = self.driver.find_element(By.XPATH, f"//li[text()='{version}']")
        selected_version.click()

    def get_all_versions(self) -> list[str]:
        all_versions: list[str] = []

        for version in self.patch_notes_versions_indicators:
            all_versions.append(version.text)
        
        return all_versions

    
