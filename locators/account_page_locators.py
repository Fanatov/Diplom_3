from selenium.webdriver.common.by import By


class AccountPageLocators:
    LOGOUT_BUTTON = By.XPATH, '//*[text()="Выход"]'
    ORDER_FEED_BUTTON = By.XPATH, "//*[text()='История заказов']"
    ORDER_FEED_LOCATION = By.XPATH, '//*[contains(@class,"OrderHistory_orderHistory")]'
    ACCOUNT_LOGOUT_BUTTON = By.XPATH, "//*[text()='Выход']"
    MAIN_PAGE_COUNT = By.XPATH, '//h2[contains(@class,"title_shadow")]'
    LAST_ORDER_NUMBER = By.XPATH, '//li[last()]//p[contains(text(), "#")]'
