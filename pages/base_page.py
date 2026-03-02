from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_new_tab_and_verify(self, main_window_handle, expected_url):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = ""

        for handle in self.driver.window_handles:
            if handle != main_window_handle:
                new_window = handle
                break

        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url))

        return True

    def close_current_tab_and_switch_back(self, main_window_handle):
        self.driver.close()
        self.driver.switch_to.window(main_window_handle)

    def click_logo_yandex(self):
        self.driver.find_element(*BasePageLocators.LOGO_YANDEX_BUTTON).click()

    def click_logo_scooter(self):
        self.driver.find_element(*BasePageLocators.LOGO_SCOOTER_BUTTON).click()

    def click_cookies_button(self):
        cookies_button = self.driver.find_elements(*BasePageLocators.COOKIES_BUTTON)
        if len(cookies_button) == 1:
            cookies_button[0].click()