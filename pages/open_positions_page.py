from selenium.webdriver.common.by import By

class OpenPositionsPage:
    positions_location_filter_location_box = (By.ID,"select2-filter-by-location-container")
    positions_location_filter_department_box = (By.ID,"select2-filter-by-department-container")
    positions_location_filter_box_list = (By.CLASS_NAME, "select2-results__options")
    positions_location_filter_name_turkey = (By.CSS_SELECTOR, ".select2-results__options > li:nth-of-type(2)")
    positions_location_turkey_first_card = (By.CSS_SELECTOR, ".position-list > div:nth-of-type(1)")
    positions_location_turkey_first_card_location = (By.CSS_SELECTOR, ".position-list > div:nth-of-type(1)> *  .position-location")
    positions_location_turkey_first_card_location_view_role = (By.CSS_SELECTOR, ".position-list > div:nth-of-type(1)> *  .btn")
    
    

