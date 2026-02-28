from selenium.webdriver.common.by import By

class BasePage:
    order_button = [By.CSS_SELECTOR, "div[class^='Header_Nav'] button[class^='Button']"]
    cookies_button = [By.ID, "rcc-confirm-button"]

    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_cookies_button(self):
        cookies_button = self.driver.find_elements(*self.cookies_button)
        if len(cookies_button) == 1:
            cookies_button[0].click()
