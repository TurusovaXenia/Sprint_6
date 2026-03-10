import pytest
from selenium import webdriver

import data


@pytest.fixture(scope='function')
def setup(request):
    driver = webdriver.Firefox()
    driver.get(data.base_url)

    request.cls.driver = driver

    yield driver
    driver.quit()
