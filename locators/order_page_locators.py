from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    PHONE_NUMBER_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")

    STATION_DROPDOWN_LIST_FIELD = (By.CSS_SELECTOR, ".select-search__input")
    STATION_DROPDOWN_LIST_ITEMS = (By.CSS_SELECTOR, ".select-search__row")

    ORDER_HEADER = (By.CSS_SELECTOR, "div[class*='Order_Header']")

    DATE_FIELD = (By.CSS_SELECTOR, ".react-datepicker__input-container input")
    RENTAL_PERIOD_DROPDOWN_LIST_FIELD = (By.CLASS_NAME, "Dropdown-root")
    RENTAL_PERIOD_DROPDOWN_LIST_ITEMS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    NEXT_BUTTON = (By.CSS_SELECTOR, "div[class*='Order_NextButton'] button")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    CHECK_STATUS_BUTTON = (By.CSS_SELECTOR, "div[class*='Order_NextButton'] button")

    SUCCESS_MODAL = (By.CSS_SELECTOR, "div[class*='Order_Modal']")
