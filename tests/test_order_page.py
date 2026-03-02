import pytest
from selenium import webdriver

from pages.order_page import OrderPage
from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HomePageLocators
import data

class TestOrderPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        'open_button, user_data',
        [
            (BasePageLocators.ORDER_BUTTON, data.user_1),
            (HomePageLocators.ORDER_BUTTON, data.user_2)
        ],
    )
    def test_order_creation_from_different_entry_points(self, open_button, user_data):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(self.driver)
        order_page.click_cookies_button()
        order_page.click_order_button(open_button)
        order_page.fill_order_form(user_data)
        order_page.click_create_order_button()
        order_page.click_confirm_order_button()

        assert "Заказ оформлен" in order_page.get_successful_message(), \
            "Окно с успешным созданием заказа не открылось"

        order_page.click_check_status_button()
        order_page.click_logo_scooter()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

        main_window = self.driver.current_window_handle
        order_page.click_logo_yandex()
        order_page.switch_to_new_tab_and_verify(main_window, "dzen.ru")

        assert "dzen.ru" in self.driver.current_url
        order_page.close_current_tab_and_switch_back(main_window)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()