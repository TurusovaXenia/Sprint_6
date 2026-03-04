import allure
import pytest
from selenium import webdriver

import data
from pages.home_page import HomePage


class TestHomePage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(data.base_url)

    @pytest.mark.parametrize("index, expected_text", data.dropdown_list_options)
    @allure.title("Проверка списка в разделе 'О важном'")
    @allure.description("Для каждого вопроса в разделе открываем его текст и проверяем на соответствие")
    def test_faq_question_shows_correct_answer(self, index, expected_text):
        home_page = HomePage(self.driver)
        home_page.click_cookies_button()

        text = home_page.get_faq_text_by_index(index)

        assert text == expected_text, \
            f"Ошибка в тексте элемента {index}"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
