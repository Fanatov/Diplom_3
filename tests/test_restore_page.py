from conftest import driver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from data import UserData
from pages.restore_password_page import RestorePasswordPage
import allure


class TestRecoverPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_click_restore_password_open_restore_password_page_success(self, driver):
        user = MainPage(driver)
        user.click_login_to_account_button()
        user = LoginPage(driver)
        user.click_restore_password()
        user = ForgotPasswordPage(driver)
        user.wait_for_restore_button_located()
        assert user.current_url() == UserData.FORGOT_PASSWORD_URL

    @allure.title('Проверка ввода почты и нажатие кнопки "Восстановить"')
    def test_click_restore_button_input_email_success(self, driver):
        user = MainPage(driver)
        user.click_login_to_account_button()
        user = LoginPage(driver)
        user.click_restore_password()
        user = ForgotPasswordPage(driver)
        user.input_email()
        user.click_restore_button()
        user = RestorePasswordPage(driver)
        user.wait_for_password_field_located()
        assert user.current_url() == UserData.RESET_PASSWORD_URL

    @allure.title('Проверка кнопки показать/скрыть')
    def test_click_secure_button_active_password_field_success(self, driver):
        user = MainPage(driver)
        user.click_login_to_account_button()
        user = LoginPage(driver)
        user.click_restore_password()
        user = ForgotPasswordPage(driver)
        user.input_email()
        user.click_restore_button()
        user = RestorePasswordPage(driver)
        user.wait_for_password_field_located()
        user.input_restore_password()
        user.wait_for_secure_button()
        user.click_secure_button()
        assert user.check_text_in_field()






