import os, time
def save_screenshot(driver, name):
    screenshots_dir = os.path.join(os.getcwd(), 'reports', 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)
    filename = f"{name}_{int(time.time())}.png"
    path = os.path.join(screenshots_dir, filename)
    driver.save_screenshot(path)
    return path
