import allure
import pytest

import data
import urls
from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators


class TestOrderPage:

    @pytest.mark.parametrize(
        'open_button, user_data',
        [
            (HeaderLocators.ORDER_BUTTON, data.user_1),
            (HomePageLocators.ORDER_BUTTON, data.user_2)
        ],
    )
    @allure.title("Проверка успешного создания заказа для двух точек входа")
    @allure.description(
        "Проходим весь позитивный флоу для создания заказа")
    def test_order_creation_from_different_entry_points(self, open_button, user_data, home_page, order_page, header):
        home_page.click_order_button(open_button)

        order_page.fill_order_form(user_data)
        order_page.click_create_order_button()
        order_page.click_confirm_order_button()

        assert order_page.check_successful_modal(), \
            "Окно с успешным созданием заказа не открылось"

    @allure.title("Проверка редиректа на главную страницу после клика на логотип 'Самоката'")
    def test_click_scooter_logo_redirects_to_home_page(self, home_page, header):
        home_page.click_order_button_header()
        header.click_logo_scooter()

        assert home_page.check_order_button_visibility(), \
            "Переход на главную страницу не выполнен"

    @allure.title("Проверка редиректа на страницу 'Дзена' после клика на логотип 'Яндекс'")
    def test_click_yandex_logo_redirects_to_dzen_page(self, home_page, header):
        header.click_logo_yandex()

        assert home_page.switch_to_new_tab(urls.EXPECTED_PAGE_URL), \
            f"Переход на страницу {urls.EXPECTED_PAGE_URL} не выполнен"
