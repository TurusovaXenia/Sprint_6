from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):
    order_button = [By.CSS_SELECTOR, "div[class^='Home_FinishButton'] button"]
    dropdown_buttons = [By.CSS_SELECTOR, ".accordion__button"]
    dropdown_options = [By.CSS_SELECTOR, ".accordion__panel p"]

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def get_item_by_index(self, index):
        dropdown_item = self.driver.find_elements(*self.dropdown_buttons)[index]
        self.driver.execute_script("arguments[0].click();", dropdown_item)
        option = (WebDriverWait(self.driver, 10).until
                  (EC.visibility_of(self.driver.find_elements(*self.dropdown_options)[index])))
        return option