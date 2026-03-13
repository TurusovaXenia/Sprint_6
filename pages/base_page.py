import random

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element_with_wait(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def fill_input(self, locator, text):
        self.wait_until_visible(locator)
        self.driver.find_element(*locator).send_keys(text)

    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Переход на новую страницу {expected_url} при нажатии на лого")
    def switch_to_new_tab(self, expected_url):
        self.wait.until(EC.number_of_windows_to_be(2))

        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

        return self.wait.until(EC.url_contains(expected_url))

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_header(self):
        self.driver.execute_script("scroll(0, 0);")

    def select_random_item_from_dropdown(self, field_locator, items_locator):
        self.click_element(field_locator)
        options = self.wait.until(
            EC.presence_of_all_elements_located(items_locator))

        random_option = random.choice(options)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_option)
        random_option.click()

    def check_element_visibility(self, locator):
        self.wait_until_visible(locator)
        return self.driver.find_element(*locator).is_displayed()

    def click_element_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)
