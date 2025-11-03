from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.first_product = (By.XPATH, "(//a[contains(@class,'product') or contains(@href,'product')])[1]")
        self.add_to_wishlist = (By.XPATH, "//button[contains(., 'Wishlist') or contains(., 'Add to wishlist')]")
        self.add_to_cart = (By.XPATH, "//button[contains(., 'Add to Cart') or contains(., 'ADD TO BAG') or contains(., 'Add to bag')]")

    def open_first_product(self):
        try:
            el = self.wait.until(EC.element_to_be_clickable(self.first_product))
            el.click()
            return True
        except Exception:
            try:
                links = self.driver.find_elements(By.XPATH, "//a[contains(@href,'product')]")
                if links:
                    links[0].click()
                    return True
            except Exception:
                return False

    def add_wishlist(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.add_to_wishlist))
            btn.click()
            return True
        except Exception:
            return False

    def add_cart(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.add_to_cart))
            btn.click()
            return True
        except Exception:
            return False
