import time
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def capture_screenshot(driver, name, extra):
    try:
        screenshot = driver.get_screenshot_as_base64()
        extra.append(pytest_html.extras.image(screenshot, name=name))
    except Exception as e:
        print(f"Screenshot failed: {e}")


@pytest.mark.usefixtures("setup_driver")
def test_firstcry_full_flow(setup_driver, extra=None):
    driver = setup_driver
    wait = WebDriverWait(driver, 60)

    try:
        # 1️⃣ Open website and login
        driver.get("https://www.firstcry.com/")
        print("✅ Website opened successfully")

        login_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'poplogin_main')]")))
        driver.execute_script("arguments[0].click();", login_icon)
        print("✅ Clicked Login/Register button")

        mobile_input = wait.until(EC.visibility_of_element_located((By.ID, "lemail")))
        mobile_input.clear()
        mobile_input.send_keys("9894652765")
        print("✅ Entered mobile number")

        continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='CONTINUE']")))
        driver.execute_script("arguments[0].click();", continue_btn)
        print("✅ Clicked Continue successfully")

        print("⚠️ Please enter OTP manually in the browser within 90 seconds...")
        otp_wait = WebDriverWait(driver, 90)
        otp_wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='search_box']")))
        print("✅ OTP entered and login successful")

        # 2️⃣ Search for product
        search_box = driver.find_element(By.ID, "search_box")
        search_box.clear()
        search_box.send_keys("baby carrier")
        search_btn = driver.find_element(By.XPATH, "//span[@class='search-button']")
        driver.execute_script("arguments[0].click();", search_btn)
        print("✅ Searched for 'baby carrier' successfully")

        # 3️⃣ Click first product & add to wishlist/cart
        first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href,'babyhug-harmony')])[1]")))
        driver.execute_script("arguments[0].click();", first_product)
        print("✅ Opened first product successfully")

        tabs = driver.window_handles
        driver.switch_to.window(tabs[-1])

        wait.until(EC.url_contains("product-detail"))
        wishlist = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@data-fc-ricon='y']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", wishlist)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", wishlist)
        print("✅ Added product to wishlist")

        add_to_cart_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(translate(text(),'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'ADD TO CART')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_btn)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", add_to_cart_btn)
        print("✅ Added product to cart")

        # 4️⃣ Go to cart and wishlist
        view_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'cart-icon')]")))
        driver.execute_script("arguments[0].click();", view_cart_btn)
        print("✅ Opened Cart page")

        time.sleep(4)
        heart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ShortlistTab1']/a/span[1]")))
        driver.execute_script("arguments[0].click();", heart_icon)
        print("✅ Opened Wishlist page")


    except Exception as e:
        driver.save_screenshot("FirstCry_Flow_Error.png")
        pytest.fail(f"❌ Test failed: {e}")
