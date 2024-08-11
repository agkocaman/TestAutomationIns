import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.base_page import BasePage
from tests.home_test import home_page_test
from tests.career_test  import home_to_career_page
from tests.career_test import career_page_test
from tests.quality_assurance_test import qa_page
from tests.open_positions_test import open_positions_filter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


import time

browser_choice = "chrome"  # change to "firefox" if you like

if browser_choice == "chrome":
    driver = webdriver.Chrome()
elif browser_choice == "firefox":
    driver = webdriver.Firefox()
else:
    print("Browser not supported")
    exit()


driver.maximize_window()

#homePage
home_page_test(driver)

#careerPage
home_to_career_page(driver)
career_page_test(driver)

#quality assurance page
qa_page(driver)

#open positions
open_positions_filter(driver)

driver.quit()
