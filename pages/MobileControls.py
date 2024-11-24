from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import DOWN_ARROW_BTN_LOC, LEFT_ARROW_BTN_LOC, RIGHT_ARROW_BTN_LOC, SHOOT_BTN_LOC, TRAP_BTN_LOC, ULT_BTN_LOC, UP_ARROW_BTN_LOC
from pages.BasePage import BasePage


class MobileControls(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # action elements
        self.shoot_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SHOOT_BTN_LOC))
        self.ult_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ULT_BTN_LOC))
        self.trap_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TRAP_BTN_LOC))
        
        # movement elements
        self.up_arrow_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(UP_ARROW_BTN_LOC))
        self.down_arrow_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(DOWN_ARROW_BTN_LOC ))
        self.left_arrow_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LEFT_ARROW_BTN_LOC))
        self.right_arrow_btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RIGHT_ARROW_BTN_LOC))
        self.movement_btns = [self.up_arrow_btn, self.down_arrow_btn, self.left_arrow_btn, self.right_arrow_btn]
    
    def send_touch_event(self, target, event_name: str = 'touchstart'):
        """
        Sends touch event to the target element.
        """
        js_script = """
            const target = arguments[0];
            const event = new Event('touchstart', { bubbles: true, cancelable: true });
            target.dispatchEvent(event);
        """

        if event_name == 'touchend':
            js_script = """
                const target = arguments[0];
                const event = new Event('touchend', { bubbles: true, cancelable: true });
                target.dispatchEvent(event);
            """

        return self.driver.execute_script(js_script, target)
