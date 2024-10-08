from selenium.webdriver.common.by import By


class RestorePageLocators:
    SAVE_BUTTON = By.XPATH, "//button[text()='Сохранить']"
    NEW_PASS_FIELD = By.XPATH, ".//input[@name = 'Введите новый пароль']"
    HIDE_UNHIDE_BUTTON = By.XPATH, '//*[@class="input__icon input__icon-action"]/*'
    RESTORE_PASSWORD_FIELD = By.XPATH, '//input[@type="text"]/following-sibling::div'
