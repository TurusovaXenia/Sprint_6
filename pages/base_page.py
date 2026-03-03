import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Переход на новую страницу {expected_url} при нажатии на лого")
    def switch_to_new_tab_and_verify(self, main_window_handle, expected_url):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = ""

        for handle in self.driver.window_handles:
            if handle != main_window_handle:
                new_window = handle
                break

        self.driver.switch_to.window(new_window)
        self.wait.until(EC.url_contains(expected_url))

    @allure.step("Закрытие второй вкладки и переход на главную страницу")
    def close_current_tab_and_switch_back(self, main_window_handle):
        self.driver.close()
        self.driver.switch_to.window(main_window_handle)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Клик по лого 'Яндекс'")
    def click_logo_yandex(self):
        self.click_element(BasePageLocators.LOGO_YANDEX_LINK)

    @allure.step("Клик по лого скутера")
    def click_logo_scooter(self):
        self.click_element(BasePageLocators.LOGO_SCOOTER_LINK)

    @allure.step("Принять использование cookie")
    def click_cookies_button(self):
        cookies_button = self.driver.find_elements(*BasePageLocators.COOKIES_BUTTON)
        if len(cookies_button) == 1:
            cookies_button[0].click()
