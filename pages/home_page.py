import time

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def get_faq_text_by_index(self, index):
        faq_item = self.wait.until(
            EC.presence_of_all_elements_located(HomePageLocators.DROPDOWN_BUTTONS)
        )[index]
        self.driver.execute_script("arguments[0].click();", faq_item)
        faq_item_text = self.wait.until(
            EC.presence_of_all_elements_located(HomePageLocators.DROPDOWN_OPTIONS)
        )[index]
        return self.wait.until(EC.visibility_of(faq_item_text)).text
