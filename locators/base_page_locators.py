from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGO_YANDEX_BUTTON = (By.CSS_SELECTOR, "a[class^='Header_LogoYandex']")
    LOGO_SCOOTER_BUTTON = (By.CSS_SELECTOR, "a[class^='Header_LogoScooter']")
    ORDER_BUTTON = (By.CSS_SELECTOR, "div[class^='Header_Nav'] button[class^='Button']")
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")