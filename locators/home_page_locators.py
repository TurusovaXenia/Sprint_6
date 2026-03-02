from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, "div[class^='Home_FinishButton'] button")
    DROPDOWN_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")
    DROPDOWN_OPTIONS = (By.CSS_SELECTOR, ".accordion__panel p")