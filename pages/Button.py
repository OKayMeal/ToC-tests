from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Button:
    def __init__(self, driver: WebDriver, button_text: str):
        self.driver = driver
        self.button_text = button_text
        
    def click_btn(self):
        """
        Waits until the button specified by 'button_text' is visible, then asserts it is displayed and clicks on it.
        Raises NoSuchElementException or TimeoutException if the button is not found or not visible within the timeout.
        """
        try:
            btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//button[text()='{self.button_text}']"))
            )

            assert btn.is_displayed(), f"{self.button_text} button is not displayed"
            btn.click()

        except Exception as e:
            # Handle exceptions or re-raise with a more informative message
            raise RuntimeError(f"Failed to click {self.button_text} button: {str(e)}")