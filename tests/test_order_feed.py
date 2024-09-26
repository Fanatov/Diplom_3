import time

from conftest import driver, popup
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccount
from pages.order_feed_page import OrderFeedPage
import allure


class TestOrderFeed:

    @allure.title('Проверка открытия окна с деталями')
    def test_click_order_opened_details_window_success(self, driver):
        user = MainPage(driver)
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        user.click_first_order_in_order_feed()
        user.wait_for_details_in_order_feed()
        assert user.check_details_in_order_feed_is_observed()

    @allure.title('Проверка отображения заказов из "История заказов" на странице "Лента заказов"')
    def test_user_orders_from_history_orders_observe_in_order_feed_success(self, driver, popup):
        user = MainPage(driver)
        user.add_bun_to_cart()
        user.click_make_order_button()
        user.click_close_ingredients_button()
        user.click_personal_account_button()
        user = PersonalAccount(driver)
        user.click_order_history_button()
        user.look_for_last_order()
        history_page_nummer = user.get_last_order_number()
        user = MainPage(driver)
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        order_feed_last_order = user.get_last_order_number()
        assert history_page_nummer == order_feed_last_order

    @allure.title('Проверка счётчика "Выполнено за всё время"')
    def test_absolete_counter_increase_after_new_order_is_created_success(self, driver, popup):
        user = MainPage(driver)
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        old_counter = user.get_absolete_counter()
        user = MainPage(driver)
        user.make_complete_order()
        user = OrderFeedPage(driver)
        user.wait_for_current_order_in_order_feed()
        new_counter = user.get_absolete_counter()
        assert new_counter > old_counter

    @allure.title('Проверка счётчика "Выполнено за сегодня"')
    def test_today_counter_increase_after_new_order_created_success(self, driver, popup):
        user = MainPage(driver)
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        old_counter = user.get_today_counter()
        user = MainPage(driver)
        user.make_complete_order()
        user = OrderFeedPage(driver)
        new_counter = user.get_today_counter()
        assert new_counter > old_counter

    @allure.title('Проверка отображения номера заказа в разделе "В работе"')
    def test_in_work_counter_is_observed_after_new_order_is_created_success(self, driver, popup):
        user = MainPage(driver)
        user.add_bun_to_cart()
        user.click_make_order_button()
        user.wait_for_order_is_loaded()
        order_counter = user.get_order_number()
        user.click_close_ingredients_button()
        user.click_order_feed_button()
        user = OrderFeedPage(driver)
        user.wait_for_work_counter_observed()
        time.sleep(2)
        in_work_counter = user.get_count_orders_in_work()
        assert order_counter == in_work_counter
