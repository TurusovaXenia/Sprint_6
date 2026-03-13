from datetime import datetime, timedelta

import allure

from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Ввод данных клиента")
    def fill_customer_info(self, name, surname, address, phone):
        self.fill_input(OrderPageLocators.NAME_FIELD, name)
        self.fill_input(OrderPageLocators.SURNAME_FIELD, surname)
        self.fill_input(OrderPageLocators.ADDRESS_FIELD, address)
        self.fill_input(OrderPageLocators.PHONE_NUMBER_FIELD, phone)

    @allure.step("Выбор рандомной станции метро")
    def set_customer_station(self):
        self.select_random_item_from_dropdown(
            OrderPageLocators.STATION_DROPDOWN_LIST_FIELD,
            OrderPageLocators.STATION_DROPDOWN_LIST_ITEMS
        )

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Ввод даты заказа самоката")
    def set_rental_date(self):
        formatted_date = (datetime.now() + timedelta(days=2)).strftime("%d.%m.%Y")
        self.find_element_with_wait(OrderPageLocators.DATE_FIELD).send_keys(formatted_date)
        self.click_element(OrderPageLocators.ORDER_HEADER)

    @allure.step("Выбор рандомного периода аренды")
    def set_rental_period(self):
        self.select_random_item_from_dropdown(
            OrderPageLocators.RENTAL_PERIOD_DROPDOWN_LIST_FIELD,
            OrderPageLocators.RENTAL_PERIOD_DROPDOWN_LIST_ITEMS
        )

    @allure.step("Клик по кнопке 'Заказать'")
    def click_create_order_button(self):
        self.click_element(OrderPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Клик по кнопке для подтверждения заказа")
    def click_confirm_order_button(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверка отображения окна об успешном создании заказа")
    def check_successful_modal(self):
       return self.check_element_visibility(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step("Заполнение формы для заказа")
    def fill_order_form(self, user_data):
        self.fill_customer_info(user_data["name"], user_data["surname"], user_data["address"], user_data["phone"])
        self.set_customer_station()
        self.click_next_button()
        self.set_rental_date()
        self.set_rental_period()
        self.click_element(OrderPageLocators.COLOR_CHECKBOX)
        self.fill_input(OrderPageLocators.COMMENT_INPUT, user_data["comment"])
