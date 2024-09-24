from selenium.webdriver.common.by import By

class LoginPageLocators:
    FORGOT_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    EMAIL_FIELD = By.XPATH, ".//input[@name = 'name']"
    PASSWORD_FIELD = By.XPATH, ".//input[@name = 'Пароль']"
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти']"
