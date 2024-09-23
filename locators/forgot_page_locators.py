from selenium.webdriver.common.by import By

class ForgorPageLocators:
    INPUT_MAIL = By.XPATH, ".//input[@name = 'name']"
    RESTORE_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    