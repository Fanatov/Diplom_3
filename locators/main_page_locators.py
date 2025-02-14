from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_HOOK = By.XPATH, "//img"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"
    ACCOUNT_BUTTON = By.XPATH, "//*[text()='Личный Кабинет']"
    MAKE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']"
    CREATE_BURGER_BUTTON = By.XPATH, '//*[text()="Конструктор"]'
    ORDER_FEED_BUTTON = By.XPATH, '//*[text()="Лента Заказов"]'
    SAUCE_SPICYX = By.XPATH, "//img[@alt = 'Соус Spicy-X']"
    SPICYX_DETAILS = By.XPATH, "//*[@class ='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"
    CLOSE_BUTTON = By.XPATH, "//section[1]//*[@type ='button']"
    CLOSE_WINDOW = By.CSS_SELECTOR, ".BurgerConstructor_basket__totalContainer__2Z-ho"
    SPICYX_COUNT = By.XPATH, "//*[@class ='counter_counter__num__3nue1'and text()='1']"
    CREATE_BURGER_BUN_DOWN = By.XPATH, '//*[text()="Перетяните булочку сюда (низ)"]'
    ORDER_READY = By.XPATH, '//*[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'
    BUN = By.XPATH, '//*[text()="Флюоресцентная булка R2-D3"]'
    ORDER_IMAGE = By.XPATH, '//div[@class="Modal_modal__P3_V5"]'
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"title_shadow")]'
