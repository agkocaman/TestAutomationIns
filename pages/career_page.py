from selenium.webdriver.common.by import By

class CareerPage:
    company_menu_item = (By.CSS_SELECTOR,".navbar-nav > li:nth-of-type(6)")
    company_menu_dropdown = (By.CSS_SELECTOR,"div.new-menu-dropdown-layout-6.show")
    company_menu_dropdown_carrier_btn = (By.CSS_SELECTOR,".new-menu-dropdown-layout-6-mid-container > a:nth-of-type(2)")
    
    career_our_location_h3 = (By.CSS_SELECTOR,"#career-our-location *  > h3")
    career_our_location_first_card = (By.CSS_SELECTOR,"#career-our-location * > ul > li:nth-of-type(1) .location-info >p.mb-0")
    
    career_teams_h3 = (By.CSS_SELECTOR,"#career-find-our-calling > * h3.category-title-media")
    career_teams_first_card = (By.CSS_SELECTOR,".career-load-more > div:nth-of-type(1) > * h3")
    
    career_life__insider_h2 = (By.CSS_SELECTOR,"section:nth-of-type(4) > * h2")
    career_life__insider_text = (By.CSS_SELECTOR,"section:nth-of-type(4) > * .elementor-widget-container >  p")
