from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.search_box = (By.ID, 'search_box')
        self.search_button = (By.XPATH, "//button[@type='submit' and (contains(., 'Search') or contains(., 'search'))]")

    def search(self, query):
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.search_box))
            el.clear()
            el.send_keys(query)
            try:
                self.driver.find_element(*self.search_button).click()
            except Exception:
                el.send_keys(Keys.ENTER)
            return True
        except Exception:
            return False
