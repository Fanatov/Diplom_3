import allure
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
