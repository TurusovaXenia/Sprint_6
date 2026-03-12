import pytest
from selenium import webdriver

import urls
from pages.header import Header
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def header(driver):
    header = Header(driver)
    return header


@pytest.fixture(scope='function')
def home_page(driver, header):
    page = HomePage(driver)
    page.go_to_url(urls.HOME_PAGE_URL)
    header.click_cookies_button()
    return page


@pytest.fixture(scope='function')
def order_page(driver, home_page):
    page = OrderPage(driver)
    return page
