from conftest import driver, popup
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccount
from data import UserData
import allure


class TestPersonalAccount:

    @allure.title('Проверка перехода в "Личный кабинет"')
    def test_open_personal_account_through_personal_account_button_success(self, driver, popup):
        user = MainPage(driver)
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.wait_for_logout_button()
        assert user.check_url_personal_account() == UserData.ACCOUNT_URL

    @allure.title('Проверка перехода в "История заказов"')
    def test_open_page_order_history_from_personal_account(self, driver, popup):
        user = MainPage(driver)
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_order_history_button()
        assert user.check_order_history_page_is_observed()

    @allure.title('Проверка выхода из аккаунта')
    def test_click_logout_button_personal_account_open_login_page_success(self, driver, popup):
        user = MainPage(driver)
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_personal_account_logout_button()
        user = LoginPage(driver)
        user.wait_login_button_to_be_located()
        assert user.current_url() == UserData.LOGIN_URL
