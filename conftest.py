import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import UserData


def pick_driver(name):
    if name == 'chrome':
        return webdriver.Chrome()
    elif name == 'firefox':
        return webdriver.Firefox()


@pytest.fixture(params=['chrome'])
def driver(request):
    driver = pick_driver(request.param)
    driver.get(UserData.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def popup(driver):
    user = MainPage(driver)
    user.wait_for_main_page_located()
    user.click_personal_account_button()
    user = LoginPage(driver)
    user.input_email()
    user.input_password()
    user.click_enter_button()
    user = MainPage(driver)
    user.wait_for_personal_account_button_located()
