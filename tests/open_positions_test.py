import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.open_positions_page import OpenPositionsPage
from pages.quality_assurance_page import QAPage
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time




    
def open_positions_filter(driver):
    try:
        # URL'ye git
        driver.get("https://useinsider.com/careers/quality-assurance/")
        wait = WebDriverWait(driver, 10)
        assert "Insider quality assurance job opportunities" in driver.title , "Insider quality assurancer not found title"
        assert driver.current_url == "https://useinsider.com/careers/quality-assurance/", "Wrong URL"
        
        driver.find_element(*QAPage.qa_button_see_all).click()
        assert driver.current_url == "https://useinsider.com/careers/open-positions/?department=qualityassurance", "Wrong URL"
        assert "Insider Open Positions | Insider" in driver.title, "Page title not found"
    

        time.sleep(10) 
        positions_location_filter_box = driver.find_element(*OpenPositionsPage.positions_location_filter_location_box)
        positions_ddepartment_filter_box = driver.find_element(*OpenPositionsPage.positions_location_filter_department_box)
        
        positions_location_filter_box.click()
    
        filter_box_list = wait.until(EC.element_to_be_clickable(OpenPositionsPage.positions_location_filter_box_list))
        assert filter_box_list.is_displayed(), "Filter box list not found"
        
        
        filter_box_list_turkey = wait.until(EC.element_to_be_clickable(OpenPositionsPage.positions_location_filter_name_turkey))
        assert filter_box_list_turkey.is_displayed(), "Filter box list Tukey not found"
        assert "Istanbul, Turkey" in filter_box_list_turkey.text

        driver.find_element(*OpenPositionsPage.positions_location_filter_name_turkey).click()
        
        filter_turkey_first_card = wait.until(EC.element_to_be_clickable(OpenPositionsPage.positions_location_turkey_first_card))
        assert filter_turkey_first_card.is_displayed(), "Filter Tukey first card not found"
        
        location_title_value = positions_location_filter_box.get_attribute('title')
        assert "Istanbul, Turkey" in location_title_value, "location_title_value not found"
        
        department_title_value = positions_ddepartment_filter_box.get_attribute('title')
        assert "Quality Assurance" in department_title_value, "department_title_value not found"
        
        filter_turkey_first_card_location = wait.until(EC.element_to_be_clickable(OpenPositionsPage.positions_location_turkey_first_card_location))
        assert filter_turkey_first_card_location.is_displayed(), "Filter Tukey first card not found"
        assert "Istanbul, Turkey" in filter_turkey_first_card_location.text, "Filter Tukey first card location not found"
        time.sleep(2)
        view_role_btn = driver.find_element(*OpenPositionsPage.positions_location_turkey_first_card_location_view_role)
        driver.execute_script("arguments[0].click();", view_role_btn)

        original_window = driver.current_window_handle
        all_windows = driver.window_handles
        
        
        # Yeni açılan sekmeye geçiş yapın
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
                
                break
    
        # Yeni sekmede bir doğrulama işlemi yapın (örneğin, sayfa başlığını kontrol edin)
        assert "Quality Assurance Engineer" in driver.title , "Insider quality assurancer not found title"
        
    except AssertionError as e:
        # Hata durumunda ekran görüntüsü al,
        BasePage.assertion_error(driver, e)

    except TimeoutException as e:
        # TimeoutException için özel bir işlem yapılabilir
        BasePage.timeout_exception_error(driver, e)


def open_positions_tests():
    browser_choice = "chrome"  # change to "firefox" if you like
    if browser_choice == "chrome":
        driver = webdriver.Chrome()
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Browser not supported")
        exit()
    driver.maximize_window()
    
    open_positions_filter(driver)

if __name__ == "__main__":
    open_positions_tests()
