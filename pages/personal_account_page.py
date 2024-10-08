import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class PersonalAccount(BasePage):

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ждём кнопку "Выйти"')
    def wait_for_logout_button(self):
        self.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверяем URL страницы "Личный кабинет"')
    def check_url_personal_account(self):
        return self.current_url()

    @allure.step('Жмём "История заказов"')
    def click_order_history_button(self):
        return self.click_element(AccountPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Ждём "История заказов"')
    def wait_for_order_page_history(self):
        return self.visibility_of_element_located(AccountPageLocators.ORDER_FEED_LOCATION)

    @allure.step('Проверяем отображения окна "История заказов"')
    def check_order_history_page_is_observed(self):
        return self.presence_of_element_detected(AccountPageLocators.ORDER_FEED_LOCATION)

    @allure.step('Жмём кнопку "Выход" в личном кабинете')
    def click_personal_account_logout_button(self):
        return self.click_element(AccountPageLocators.ACCOUNT_LOGOUT_BUTTON)

    @allure.step('Ищем последний заказ')
    def look_for_last_order(self):
        return self.execute_script(AccountPageLocators.LAST_ORDER_NUMBER)

    @allure.step('Получаем номер последнего заказа')
    def get_last_order_number(self):
        return self.get_text(AccountPageLocators.LAST_ORDER_NUMBER)
