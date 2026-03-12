from selenium.webdriver.common.by import By


class HomePageLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, "div[class*='Home_FinishButton'] button")
    QUESTION_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")
    ANSWER_LOCATOR = (By.CSS_SELECTOR, ".accordion__panel p")
    QUESTION_LOCATOR_TO_SCROLL = (By.ID, "accordion__heading-7")
