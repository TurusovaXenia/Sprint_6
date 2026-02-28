import pytest
from selenium import webdriver
from pages.home_page import HomePage
import data

class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("index, expected_text", data.dropdown_list_options)
    def test_dropdown_list_items(self, index, expected_text):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePage(self.driver)
        home_page.click_cookies_button()

        item = home_page.get_item_by_index(index)

        assert item.text == expected_text, f"Ошибка в тексте элемента {index}"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()