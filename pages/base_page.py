from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def click_element(self, locator):  # Клик на элемент
        element = self.wait_element_to_be_clickable(locator)
        return element.click()

    def input_text(self, locator, text):
        element = self.visibility_of_element_located(locator)
        element.clear()
        return element.send_keys(text)

    def current_url(self):
        return self.driver.current_url

    def visibility_of_element_located(self, locator):  # Ожидание отображения элемента
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def presence_of_element_detected(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    def check_element_is_displayed(self, locator):
        return self.visibility_of_element_located(locator).is_displayed()

    def drag_and_drop_elements(self, first_locator, second_locator):
        start = self.visibility_of_element_located(first_locator)
        end = self.presence_of_element_detected(second_locator)
        return drag_and_drop(self.driver, start, end)

    def get_text(self, locator):
        return self.presence_of_element_detected(locator).text

    def scroll_to_element(self, locator):
        element = self.visibility_of_element_located(locator)
        return self.driver.scroll_to_element("arguments[0].scrollIntoView();", element)
