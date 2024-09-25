import allure
from pages.base_page import BasePage
from locators.restore_page_locators import RestorePageLocators
from data import UserData


class RestorePasswordPage(BasePage):
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ждём поле "Пароль"')
    def wait_for_password_field_located(self):
        return self.visibility_of_element_located(RestorePageLocators.NEW_PASS_FIELD)

    @allure.step('Проверяем URL страницы "Восстановить пароль"')
    def check_restore_page_url(self):
        return self.current_url()

    @allure.step('Жмём "Восстановить Пароль"')
    def input_restore_password(self):
        return self.input_text(RestorePageLocators.NEW_PASS_FIELD, UserData.STATIC_PASSWORD)

    @allure.step('Ждём кнопку показать/скрыть')
    def wait_for_secure_button(self):
        return self.visibility_of_element_located(RestorePageLocators.HIDE_UNHIDE_BUTTON)

    @allure.step('Жмём кнопку показать/скрыть')
    def click_secure_button(self):
        return self.click_element(RestorePageLocators.HIDE_UNHIDE_BUTTON)

    @allure.step('Проверяем отображение текста в поле "Восстановить пароль"')
    def check_text_in_field(self):
        return self.check_element_is_displayed(RestorePageLocators.RESTORE_PASSWORD_FIELD)

