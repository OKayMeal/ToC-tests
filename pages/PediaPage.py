from selenium.webdriver.remote.webdriver import WebDriver
from pages.BasePage import BasePage
from pages.Button import Button
from locators.locators import BTN_TEXT_LOCATORS, PEDIA_CARD_LOC, PEDIA_RECORD_NAME_DIV_LOC, PEDIA_RECORD_NAME_TEXT_LOC, PEDIA_STAT_LOC, RECORDS_CARD_LOC, RECORDS_IMAGES_GENERIC_LOC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PediaPage(BasePage):
    def __init__(self, driver: WebDriver, name: str):
        super().__init__(driver)
        self.name = name

        # elements
        self.records_card = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RECORDS_CARD_LOC))
        self.records_images = self.records_card.find_elements(*RECORDS_IMAGES_GENERIC_LOC)
        self.pedia_card = driver.find_element(*PEDIA_CARD_LOC)
        self.pedia_record_name = driver.find_element(*PEDIA_RECORD_NAME_DIV_LOC).find_element(*PEDIA_RECORD_NAME_TEXT_LOC)
        self.back_btn = Button(driver, BTN_TEXT_LOCATORS['back'])
        
        if self.name == 'BESTIARY':
            self.ng_btn = Button(driver, BTN_TEXT_LOCATORS['ng+'])
    
    
    def select_record(self, name: str):
        """
        Selects pedia record to display.
        @param name - name of the record to display
        """
        for portrait in self.records_images:
            if portrait.get_attribute('alt') == name:
                portrait.click()
                self.pedia_selected_record_image = self.pedia_card.find_element(*RECORDS_IMAGES_GENERIC_LOC)
                self.pedia_selected_record_stats = self.pedia_card.find_elements(*PEDIA_STAT_LOC)
                


    def get_all_stats(self):
        """
        Gets all displayed record's stats
        """

        if self.pedia_selected_record_stats and len(self.pedia_selected_record_stats) > 0:
            all_stats: list[int] = []

            for stat in self.pedia_selected_record_stats:
                if '----' in stat.text:
                    stat_value = 0
                else:
                    stat_value = self.parse_stat_text(stat.text)
                    
                all_stats.append(stat_value)

            return all_stats

        

    def get_all_records_names(self) -> list[str]:
        """
        Gets all displayed records names in Pedia
        """

        records_names: list[str] = []
        for record in self.records_images:
            records_names.append(record.get_attribute('alt'))
        
        return records_names
    

    def parse_stat_text(self, text: str):
        """
        Get the number value from stat text for example 'hp: 10', get the value 10
        """

        parts = text.split(':')

        return int(parts[1].strip())

