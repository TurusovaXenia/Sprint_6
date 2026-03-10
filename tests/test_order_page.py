import allure
import pytest

import data
from locators.base_page_locators import BasePageLocators
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrderPage:
    driver = None

    @pytest.mark.parametrize(
        'open_button, user_data',
        [
            (BasePageLocators.ORDER_BUTTON, data.user_1),
            (HomePageLocators.ORDER_BUTTON, data.user_2)
        ],
    )
    @allure.title("Проверка успешного создания заказа для двух точек входа")
    @allure.description(
        "Проходим весь позитивный флоу для создания заказа, проверяем редиректы на страницы при нажатии на лого")
    def test_order_creation_from_different_entry_points(self, open_button, user_data, setup):
        home_page = HomePage(self.driver)
        home_page.click_cookies_button()
        home_page.click_order_button(open_button)

        order_page = OrderPage(self.driver)
        order_page.fill_order_form(user_data)
        order_page.click_create_order_button()
        order_page.click_confirm_order_button()

        assert "Заказ оформлен" in order_page.get_successful_message(), \
            "Окно с успешным созданием заказа не открылось"

        order_page.click_check_status_button()
        order_page.click_logo_scooter()
        assert self.driver.current_url == data.base_url, \
            "Переход на главную страницу не выполнен"

        order_page.click_logo_yandex()
        order_page.switch_to_new_tab_and_verify(data.expected_page_url)

        assert data.expected_page_url in self.driver.current_url, \
                "Переход на страницу Дзена не выполнен"
