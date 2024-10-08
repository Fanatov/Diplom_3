import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import UserData


class LoginPage(BasePage):

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Жмём "Восстановить пароль".')
    def click_restore_password(self):
        return self.click_element(LoginPageLocators.FORGOT_PASSWORD)

    @allure.step('Ввод email')
    def input_email(self):
        return self.input_text(LoginPageLocators.EMAIL_FIELD, UserData.STATIC_EMAIL)

    @allure.step('Ввод пароля')
    def input_password(self):
        return self.input_text(LoginPageLocators.PASSWORD_FIELD, UserData.STATIC_PASSWORD)

    @allure.step('Жмём "Войти"')
    def click_enter_button(self):
        return self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Ждём кнопку "Войти"')
    def wait_login_button_to_be_located(self):
        return self.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
