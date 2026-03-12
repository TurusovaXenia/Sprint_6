import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step("Получить текст ответа для вопроса с индексом {index}")
    def get_faq_text_by_index(self, index):
        with allure.step("Кликаем на вопрос"):
            faq_item = self.wait.until(
            EC.presence_of_all_elements_located(HomePageLocators.QUESTION_BUTTONS))[index]

            self.scroll_to_element(HomePageLocators.QUESTION_LOCATOR_TO_SCROLL)
            self.driver.execute_script("arguments[0].click();", faq_item)

        with allure.step("Получаем ответ на вопрос"):
            faq_item_text = self.wait.until(
            EC.presence_of_all_elements_located(HomePageLocators.ANSWER_LOCATOR))[index]
            return self.wait.until(EC.visibility_of(faq_item_text)).text

    @allure.step("Клик по кнопке 'Заказать'")
    def click_order_button(self, button_locator):
        self.click_element(button_locator)

    @allure.step("Проверка перехода на главную страницу сервиса")
    def check_order_button_visibility(self):
        self.scroll_to_element(HomePageLocators.ORDER_BUTTON)
        return self.driver.find_element(*HomePageLocators.ORDER_BUTTON).is_displayed()
