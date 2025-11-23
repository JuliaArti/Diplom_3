from selenium.webdriver.support.wait import WebDriverWait

from locators.header_locators import LocatorsHeader

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def go_to_constructor(self):
        self.driver.find_element(*LocatorsHeader.CONSTRUCTOR_BUTTON).click()
        # return ConstructorPage(self.driver)
    
    def go_to_order_feed(self):
        self.driver.find_element(*LocatorsHeader.ORDER_FEED_BUTTON).click()
        # return OrderFeedPage(self.driver)
    
    def go_to_account(self):
        self.driver.find_element(*LocatorsHeader.ACCOUNT_BUTTON).click()
        # return AccountPage(self.driver)
    
    def go_to_main_via_logo(self):
        self.driver.find_element(*LocatorsHeader.LOGO).click()
        # return MainPage(self.driver)