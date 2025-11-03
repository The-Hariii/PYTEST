from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.sign_in_button = (By.XPATH, "//a[contains(text(),'Sign In') or contains(text(),'Sign in') or contains(text(),'Sign In / Sign Up')]")
        self.mobile_input = (By.ID, 'loginMobile')
        self.continue_btn = (By.XPATH, "//button[normalize-space()='CONTINUE' or contains(., 'Continue')]")
        self.search_box = (By.ID, 'search_box')

    def open_signin(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.sign_in_button))
            btn.click()
            return True
        except Exception:
            return False

    def enter_mobile(self, mobile):
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.mobile_input))
            el.clear()
            el.send_keys(str(mobile))
            return True
        except Exception:
            return False

    def click_continue(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.continue_btn))
            btn.click()
            return True
        except Exception:
            return False

    def wait_for_search_box(self, timeout=90):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.search_box))
            return True
        except Exception:
            return False
