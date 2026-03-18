import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):

    @allure.step("Клик по лого 'Яндекс'")
    def click_logo_yandex(self):
        self.scroll_to_header()
        self.click_element(HeaderLocators.LOGO_YANDEX_LINK)

    @allure.step("Клик по лого скутера")
    def click_logo_scooter(self):
        self.click_element(HeaderLocators.LOGO_SCOOTER_LINK)

    @allure.step("Принять использование cookie")
    def click_cookies_button(self):
        cookies_button = self.find_elements_with_wait(HeaderLocators.COOKIES_BUTTON)
        if len(cookies_button) > 0:
            cookies_button[0].click()
