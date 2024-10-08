import allure

from pages.base_page import BasePage
from locators.forgot_page_locators import ForgorPageLocators
from conftest import driver
from data import UserData


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ждём "Восстановить пароль"')
    def wait_for_restore_button_located(self):
        return self.visibility_of_element_located(ForgorPageLocators.RESTORE_BUTTON)

    @allure.step('Проверяем URL')
    def check_restore_password_url(self):
        return self.current_url()

    @allure.step('Ввод email')
    def input_email(self):
        return self.input_text(ForgorPageLocators.INPUT_MAIL, UserData.STATIC_EMAIL)

    @allure.step('Жмём  "Восстановить пароль"')
    def click_restore_button(self):
        return self.click_element(ForgorPageLocators.RESTORE_BUTTON)
