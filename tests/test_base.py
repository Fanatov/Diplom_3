import time
import allure
from conftest import driver, popup
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import UserData


class TestBase:

    @allure.title('Проверка перехода в "Конструктор"')
    def test_open_constructor_page_from_login_page_success(self, driver):
        user = MainPage(driver)
        user.click_login_to_account_button()
        user = LoginPage(driver)
        user.wait_login_button_to_be_located()
        user = MainPage(driver)
        user.click_constructor_button()
        user.wait_for_main_page_located()
        assert user.current_url() == UserData.MAIN_PAGE_URL

    @allure.title('Проверка перехода в "Лента заказов"')
    def test_click_order_feed_field_open_order_feed_page_success(self, driver):
        user = MainPage(driver)
        user.click_order_feed_button()
        user.wait_for_url_order_feed()
        assert user.current_url() == UserData.ORDER_FEED_URL

    @allure.title('Проверка открытия окна с деталями ингридиента')
    def test_click_ingredient_opened_details_success(self, driver):
        user = MainPage(driver)
        user.click_ingredient_sauce()
        user.wait_for_sauce_ingredient_details()
        assert user.check_ingridient_details_observed()

    @allure.title('Проверка закрытия всплывающего окна')
    def test_click_close_button_ingredient_closed_details_window_success(self, driver):
        user = MainPage(driver)
        user.click_ingredient_sauce()
        user.wait_for_sauce_ingredient_details()
        user.click_close_ingredients_button()
        user.wait_for_details_ingredients_window_is_closed()
        assert user.check_details_ingredients_window_is_closed()

    @allure.title('Проверка что счётчик ингредиента увеличивается')
    def test_add_ingredient_sauce_to_cart_change_counter_success(self, driver):
        user = MainPage(driver)
        user.sauce_add_to_cart()
        assert user.check_change_sauce_count() == '1'

    @allure.title('Проверка оформления заказа зарегистрированным пользователем')
    def test_click_place_order_logged_user_new_order_success(self, driver, popup):
        user = MainPage(driver)
        user.wait_for_make_order_is_located()
        user.click_make_order_button()
        user.wait_for_order_page_located()
        assert user.check_order_complete_window()
