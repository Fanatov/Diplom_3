import pytest
from selenium import webdriver

import data


def pick_driver(driver):
    if driver == 'chrome':
        return webdriver.Chrome()
    elif driver == 'firefox':
        return webdriver.Firefox()


@pytest.fixture(params=['chrome'])
def driver(request):
    driver = pick_driver(request.param)
    driver.get(DATA.Urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()
