import random
from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    def click_order_button(self, button_locator):
        self.driver.find_element(*button_locator).click()

    def set_customer_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_customer_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_customer_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_customer_station(self):
        self.driver.find_element(*OrderPageLocators.STATION_DROPDOWN_LIST_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.STATION_DROPDOWN_LIST_ITEMS)
        )
        options = self.driver.find_elements(*OrderPageLocators.STATION_DROPDOWN_LIST_ITEMS)

        random_option = random.choice(options)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_option)
        random_option.click()

    def set_customer_phone(self, phone):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            OrderPageLocators.PHONE_NUMBER_FIELD
        )).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def set_rental_date(self):
        tomorrow_after = datetime.now() + timedelta(days=2)
        formatted_date = tomorrow_after.strftime("%d.%m.%Y")
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(formatted_date)
        self.driver.find_element(*OrderPageLocators.ORDER_HEADER).click()

    def set_rental_period(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN_LIST_BUTTON).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_DROPDOWN_LIST_ITEMS)
        )
        options = self.driver.find_elements(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN_LIST_ITEMS)
        random_option = random.choice(options)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_option)
        random_option.click()

    def set_scooter_color(self):
        self.driver.find_element(*OrderPageLocators.COLOR_CHECKBOX).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    def click_create_order_button(self):
        self.driver.find_element(*OrderPageLocators.CREATE_ORDER_BUTTON).click()

    def click_confirm_order_button(self):
        self.driver.find_element(*OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    def get_successful_message(self):
        modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL))
        return modal.find_element(*OrderPageLocators.SUCCESS_MODAL).text

    def fill_order_form(self, user_data):
        self.set_customer_name(user_data["name"])
        self.set_customer_surname(user_data["surname"])
        self.set_customer_address(user_data["address"])
        self.set_customer_station()
        self.set_customer_phone(user_data["phone"])
        self.click_next_button()
        self.set_rental_date()
        self.set_rental_period()
        self.set_scooter_color()
        self.set_comment(user_data["comment"])

    def click_check_status_button(self):
        self.driver.find_element(*OrderPageLocators.CHECK_STATUS_BUTTON).click()