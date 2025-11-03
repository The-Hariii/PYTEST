import pytest, os, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def browser():
    opts = Options()
    opts.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
    yield driver
    driver.quit()

# Save screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('browser')
        if driver is not None:
            screenshots_dir = os.path.join(os.getcwd(), 'reports', 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            path = os.path.join(screenshots_dir, f"{item.name}_{int(time.time())}.png")
            try:
                driver.save_screenshot(path)
            except Exception:
                pass
