from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartWishlistPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.cart_icon = (By.XPATH, "//a[contains(@href,'cart') or contains(@class,'cart')]")
        self.wishlist_icon = (By.XPATH, "//a[contains(@href,'wishlist') or contains(@class,'wishlist')]")
        self.remove_buttons = (By.XPATH, "//button[contains(., 'Remove') or contains(., 'Remove Item') or contains(., 'Remove from cart')]")

    def open_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()
            return True
        except Exception:
            return False

    def open_wishlist(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.wishlist_icon)).click()
            return True
        except Exception:
            return False

    def remove_any_item(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.remove_buttons))
            btn.click()
            return True
        except Exception:
            return False
