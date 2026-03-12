import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):

    @allure.step("Клик по лого 'Яндекс'")
    def click_logo_yandex(self):
        self.driver.execute_script("scroll(0, 0);")
        self.click_element(HeaderLocators.LOGO_YANDEX_LINK)

    @allure.step("Клик по лого скутера")
    def click_logo_scooter(self):
        self.click_element(HeaderLocators.LOGO_SCOOTER_LINK)

    @allure.step("Принять использование cookie")
    def click_cookies_button(self):
        cookies_button = self.driver.find_elements(*HeaderLocators.COOKIES_BUTTON)
        if len(cookies_button) > 0:
            cookies_button[0].click()
