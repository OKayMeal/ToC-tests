from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import ATK_STATS_LOC, DEF_STATS_LOC, ENEMIES_INDICATOR_LOC, ENEMIES_LABEL_LOC, EQUIPMENT_CONTAINER_LOC, GOLD_INDICATOR_LOC, HEARTS_CONTAINER_LOC, HEARTS_LOC, HP_INDICATOR_LOC, KEYS_INDICATOR_LOC, KEYS_LABEL_LOC, LVL_STATS_LOC, SETTINGS_HUD_BTN_LOC, SPEED_STATS_LOC, STATS_CONTAINER_LOC, TRAPS_INDICATOR_LOC, TRAPS_LABEL_LOC, ULT_CHARGE_INDICATOR_LOC, ULT_IMAGE_LOC, ULT_LABEL_LOC
from pages.BasePage import BasePage

class GameHUD(BasePage):
    def __init__(self, driver: WebDriver, ult_ready: bool = True):
        super().__init__(driver)

        # elements
        self.settings_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SETTINGS_HUD_BTN_LOC))
        self.hearts_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HEARTS_CONTAINER_LOC))
        self.hearts = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HEARTS_LOC))
        self.hp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HP_INDICATOR_LOC))
        self.stats_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(STATS_CONTAINER_LOC))
        self.level = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LVL_STATS_LOC))
        self.attack = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ATK_STATS_LOC))
        self.defense =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located(DEF_STATS_LOC))
        self.speed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SPEED_STATS_LOC))
        self.equipment_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EQUIPMENT_CONTAINER_LOC))
        self.gold = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(GOLD_INDICATOR_LOC))
        self.ult_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ULT_LABEL_LOC))
        if ult_ready:
            self.ult_image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ULT_IMAGE_LOC))
        else:
            self.ult_charge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ULT_CHARGE_INDICATOR_LOC))
        self.traps_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TRAPS_LABEL_LOC))
        self.traps = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TRAPS_INDICATOR_LOC))
        self.keys_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(KEYS_LABEL_LOC))
        self.keys = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(KEYS_INDICATOR_LOC))
        self.enemies_left_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ENEMIES_LABEL_LOC))
        self.enemies_left = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ENEMIES_INDICATOR_LOC))