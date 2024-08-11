import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.home_page import HomePage
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

import time


    
def home_page_test(driver):
    try:
        # URL'ye git
        driver.get("https://useinsider.com/")
        wait = WebDriverWait(driver, 10)
        assert "Insider" in driver.title , "Insider not found"
        assert driver.current_url == "https://useinsider.com/", "Wrong URL"
        demo_button = wait.until(EC.element_to_be_clickable(HomePage.DEMO_BUTTON))
        assert demo_button.is_displayed(), "Demo button not found"
        logo_img = wait.until(EC.element_to_be_clickable(HomePage.LOGO_IMG))
        assert logo_img.is_displayed(), "Logo not found"

    except AssertionError as e:
        # Hata durumunda ekran görüntüsü al,
        BasePage.assertion_error(driver, e)

    except TimeoutException as e:
        # TimeoutException için özel bir işlem yapılabilir
        BasePage.timeout_exception_error(driver, e)

def home_tests():
    browser_choice = "chrome"  # change to "firefox" if you like
    if browser_choice == "chrome":
        driver = webdriver.Chrome()
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Browser not supported")
        exit()
    driver.maximize_window()
    
    home_page_test(driver)

if __name__ == "__main__":
    home_tests()
