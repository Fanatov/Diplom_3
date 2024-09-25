import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from data import UserData


class OrderFeedPage(BasePage):
    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ждём первый заказ в "Лента заказов"')
    def wait_for_current_order_in_order_feed(self):
        return self.wait_element_to_be_clickable(OrderFeedLocators.FIRST_ORDER)

    @allure.step('Жмём на первый заказ')
    def click_first_order_in_order_feed(self):
        return self.click_element(OrderFeedLocators.FIRST_ORDER)

    @allure.step('Ждём окно деталей заказа')
    def wait_for_details_in_order_feed(self):
        return self.presence_of_element_detected(OrderFeedLocators.DETAILS_WINDOW)

    @allure.step('Проверяем окно деталей заказа')
    def check_details_in_order_feed_is_observed(self):
        return self.check_element_is_displayed(OrderFeedLocators.DETAILS_WINDOW)

    @allure.step('Получаем заказы "За все время"')
    def get_absolete_counter(self):
        return self.get_text(OrderFeedLocators.ABSOLETE_COUNTER)

    @allure.step('Получаем заказы "За сегодня"')
    def get_today_counter(self):
        return self.get_text(OrderFeedLocators.TODAY_COUNTER)

    @allure.step('Ждём заказы "В работе"')
    def wait_for_work_counter_observed(self):
        return self.presence_of_element_detected(OrderFeedLocators.CURRENT_ORDERS)

    @allure.step('Получаем количество заказов "В работе"')
    def get_count_orders_in_work(self):
        count = self.get_text(OrderFeedLocators.CURRENT_ORDERS)[1::]
        return count

    @allure.step('Получаем номер последнего заказа')
    def get_last_order_number(self):
        return self.get_text(OrderFeedLocators.LAST_ORDER_NUMBER)
