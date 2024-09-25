import time

import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import UserData


class MainPage(BasePage):

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ждём главную страницу')
    def wait_for_main_page_located(self):
        return self.visibility_of_element_located(MainPageLocators.MAIN_PAGE_HOOK)

    @allure.step('Жмём "Войти в аккаунт"')
    def click_login_to_account_button(self):
        return self.click_element(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Жмём "Личный кабинет"')
    def click_personal_account_button(self):
        return self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Ждём кнопку "Личный кабинет"')
    def wait_for_personal_account_button_located(self):
        return self.visibility_of_element_located(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Жмём "Конструктор"')
    def click_constructor_button(self):
        return self.click_element(MainPageLocators.CREATE_BURGER_BUTTON)

    @allure.step('Жмём "Лента заказов"')
    def click_order_feed_button(self):
        return self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Ждём URL страницы "Лента заказов"')
    def wait_for_url_order_feed(self):
        return self.wait_for_url(UserData.ORDER_FEED_URL)

    @allure.step('Жмём ингредиент - соус')
    def click_ingredient_sauce(self):
        return self.click_element(MainPageLocators.SAUCE_SPICYX)

    @allure.step('Ждём детали соуса')
    def wait_for_sauce_ingredient_details(self):
        return self.presence_of_element_detected(MainPageLocators.SPICYX_DETAILS)

    @allure.step('Проверка отображения окна деталей соуса')
    def check_ingridient_details_observed(self):
        return self.presence_of_element_detected(MainPageLocators.SPICYX_DETAILS).is_displayed()

    @allure.step('Жмём кнопку "закрыть"')
    def click_close_ingredients_button(self):
        time.sleep(1)
        return self.click_element(MainPageLocators.CLOSE_BUTTON)

    @allure.step('Ждём окно с деталями')
    def wait_for_details_ingredients_window_is_closed(self):
        return self.presence_of_element_detected(MainPageLocators.CLOSE_WINDOW)

    @allure.step('Проверяем закрытие окна с деталями')
    def check_details_ingredients_window_is_closed(self):
        return self.check_element_is_displayed(MainPageLocators.CLOSE_WINDOW)

    @allure.step('Ждём отображение соуса')
    def wait_for_sauce_is_located(self):
        return self.visibility_of_element_located(MainPageLocators.SAUCE_SPICYX)

    @allure.step('Добавляем соус')
    def sauce_add_to_cart(self):
        return self.drag_and_drop_elements(MainPageLocators.SAUCE_SPICYX,
                                                    MainPageLocators.CREATE_BURGER_BUN_DOWN)

    @allure.step('Проверяем изменение')
    def check_change_sauce_count(self):
        return self.get_text(MainPageLocators.SPICYX_COUNT)

    @allure.step('Ждём кнопку "Оформить заказ"')
    def wait_for_make_order_is_located(self):
        return self.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Ждём "Оформить заказ"')
    def click_make_order_button(self):
        return self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Ждём появление "Заказ оформлен"')
    def wait_for_order_is_loaded(self):
        return self.visibility_of_element_located(MainPageLocators.ORDER_IMAGE)

    @allure.step('Ждём окно "Заказ оформлен"')
    def wait_for_order_page_located(self):
        return self.visibility_of_element_located(MainPageLocators.ORDER_READY)

    @allure.step('Проверяем отображение окна "Заказ оформлен"')
    def check_order_complete_window(self):
        return self.presence_of_element_detected(MainPageLocators.ORDER_READY).is_displayed()

    @allure.step('Добавляем бургер')
    def add_bun_to_cart(self):
        return self.drag_and_drop_elements(MainPageLocators.BUN_N200I,
                                                    MainPageLocators.CREATE_BURGER_BUN_DOWN)

    @allure.step('Создаем заказ')
    def make_complete_order_n200_bun(self):
        self.click_constructor_button()
        self.add_bun_to_cart()
        self.click_make_order_button()
        self.click_close_ingredients_button()
        self.click_order_feed_button()

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        count = self.get_text(MainPageLocators.ORDER_NUMBER)
        return count

