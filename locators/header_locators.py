from selenium.webdriver.common.by import By


class HeaderLocators:
    ORDER_BUTTON = (By.CSS_SELECTOR, "div[class^='Header_Nav'] button[class^='Button']")
    LOGO_YANDEX_LINK = (By.CSS_SELECTOR, "a[class*='Header_LogoYandex']")
    LOGO_SCOOTER_LINK = (By.CSS_SELECTOR, "a[class*='Header_LogoScooter']")
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")
