import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.quality_assurance_page import QAPage
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


    
def qa_page(driver):
    try:
        # URL'ye git
        driver.get("https://useinsider.com/careers/quality-assurance/")
        wait = WebDriverWait(driver, 10)
        assert "Insider quality assurance job opportunities" in driver.title , "Insider quality assurancer not found title"
        assert driver.current_url == "https://useinsider.com/careers/quality-assurance/", "Wrong URL"
        
        qa_h1 = wait.until(EC.element_to_be_clickable(QAPage.qa_h1))
        assert qa_h1.is_displayed(), "QA h1 not found"
        assert "Quality Assurance" in qa_h1.text, "Quality Assurance text not found"
        
        qa_see_all_btn = wait.until(EC.element_to_be_clickable(QAPage.qa_button_see_all))
        assert qa_see_all_btn.is_displayed(), "QA see all button not found"
        assert "See all QA jobs" in qa_see_all_btn.text, "QA see all button text not found"
        
        driver.find_element(*QAPage.qa_button_see_all).click()
        assert driver.current_url == "https://useinsider.com/careers/open-positions/?department=qualityassurance", "Wrong URL"
        assert "Insider Open Positions | Insider" in driver.title, "Page title not found"
        
        
        
    except AssertionError as e:
        # Hata durumunda ekran görüntüsü al,
        BasePage.assertion_error(driver, e)

    except TimeoutException as e:
        # TimeoutException için özel bir işlem yapılabilir
        BasePage.timeout_exception_error(driver, e)


def qa_tests():
    browser_choice = "chrome"  # change to "firefox" if you like
    if browser_choice == "chrome":
        driver = webdriver.Chrome()
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Browser not supported")
        exit()
    driver.maximize_window()
    
    qa_page(driver)

if __name__ == "__main__":
    qa_tests()
