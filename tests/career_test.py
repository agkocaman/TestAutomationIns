import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.career_page import CareerPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


    
def home_to_career_page(driver):
    try:
        # URL'ye git
        driver.get("https://useinsider.com/")
        wait = WebDriverWait(driver, 10)
        assert "Insider" in driver.title , "Insider not found"
        assert driver.current_url == "https://useinsider.com/", "Wrong URL"
        demo_button = wait.until(EC.element_to_be_clickable(HomePage.DEMO_BUTTON))
        assert demo_button.is_displayed(), "Demo button not found"
        
        company_menu_item = driver.find_element(*CareerPage.company_menu_item)
        assert company_menu_item.is_displayed(), "Company menu item not found"
        assert "Company" in company_menu_item.text, "Company menu item text not found"
        
        driver.find_element(*CareerPage.company_menu_item).click()
        
        company_menu_dropdown = driver.find_element(*CareerPage.company_menu_dropdown)
        assert company_menu_dropdown.is_displayed(), "Company menu dropdown not found"
        
        company_menu_dropdown_carrier_btn = driver.find_element(*CareerPage.company_menu_dropdown_carrier_btn)
        assert company_menu_dropdown_carrier_btn.is_displayed(), "Company menu dropdown carrier button not found"
        assert "Careers" in company_menu_dropdown_carrier_btn.text, "Company menu dropdown carrier button text not found"
        
        company_menu_dropdown_carrier_btn.click()
        
        assert driver.current_url == "https://useinsider.com/careers/", "Wrong URL"
        assert "Ready to disrupt? | Insider Careers" in driver.title, "Page title not found"
        
        
    except AssertionError as e:
        # Hata durumunda ekran görüntüsü al,
        BasePage.assertion_error(driver, e)

    except TimeoutException as e:
        # TimeoutException için özel bir işlem yapılabilir
        BasePage.timeout_exception_error(driver, e)

def career_page_test(driver):
    try:
        # URL'ye git
        driver.get("https://useinsider.com/careers/")
        assert driver.current_url == "https://useinsider.com/careers/", "Wrong URL"
        assert "Ready to disrupt? | Insider Careers" in driver.title, "Page title not found"
        
        #location
        our_location_h3 = driver.find_element(*CareerPage.career_our_location_h3)
        assert our_location_h3.is_displayed(), "Our location h3 not found"
        assert "Our Locations" in our_location_h3.text, "Our location h3 text not found"
        our_location_first_card_name = driver.find_element(*CareerPage.career_our_location_first_card)
        assert our_location_first_card_name.is_displayed(), "Our location first name not found"
        assert "New York" in our_location_first_card_name.text, "Our location first name text not found"
        
        #teams
        teams_h3 = driver.find_element(*CareerPage.career_teams_h3)
        assert teams_h3.is_displayed(), "Teams h3 not found"
        assert "Find your calling" in teams_h3.text, "Teams h3 text not found"
        teams_first_card_name = driver.find_element(*CareerPage.career_teams_first_card)
        assert teams_first_card_name.is_displayed(), "Teams first name not found"
        assert "Customer Success" in teams_first_card_name.text, "Teams first name text not found"
        
        #Life
        life_h2 = driver.find_element(*CareerPage.career_life__insider_h2)
        assert life_h2.is_displayed(), "Life h2 not found"
        assert "Life at Insider" in life_h2.text, "Life h2 text not found"
        life_text = driver.find_element(*CareerPage.career_life__insider_text)
        assert life_text.is_displayed(), "Life text not found"
        assert "We’re here to grow and drive growth" in life_text.text, "Life text not found"
        
    except AssertionError as e:
        # Hata durumunda ekran görüntüsü al,
        BasePage.assertion_error(driver, e)

    except TimeoutException as e:
        # TimeoutException için özel bir işlem yapılabilir
        BasePage.timeout_exception_error(driver, e)


def career_tests():
    browser_choice = "chrome"  # change to "firefox" if you like
    if browser_choice == "chrome":
        driver = webdriver.Chrome()
    elif browser_choice == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Browser not supported")
        exit()
    driver.maximize_window()
    
    home_to_career_page(driver)
    career_page_test(driver)

if __name__ == "__main__":
    career_tests()
