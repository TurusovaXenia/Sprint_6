from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def get_item_by_index(self, index):
        dropdown_item = self.driver.find_elements(*HomePageLocators.DROPDOWN_BUTTONS)[index]
        self.driver.execute_script("arguments[0].click();", dropdown_item)
        option = (WebDriverWait(self.driver, 10).until
                  (EC.visibility_of(self.driver.find_elements(*HomePageLocators.DROPDOWN_OPTIONS)[index])))
        return option