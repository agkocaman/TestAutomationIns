from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class BasePage:
    base_url = "https://useinsider.com/"
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def take_screenshot(self, step_name):
        filename = step_name + "_error.png"
        self.driver.save_screenshot(filename)
    def assertion_error(self, e):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"screenshot_{e.args[0]}_{timestamp}.png"
        screenshot_name = screenshot_name.replace(" ", "_").replace(":", "").replace("/", "")
        self.save_screenshot(screenshot_name)
        print(f"Assertion failed, screenshot taken: {screenshot_name}")
    def timeout_exception_error(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"screenshot_TimeoutException_{timestamp}.png"
        screenshot_name = screenshot_name.replace(" ", "_").replace(":", "").replace("/", "")
        self.save_screenshot(screenshot_name)
        print(f"Ekran görüntüsü adı: {screenshot_name}")