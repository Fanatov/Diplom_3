from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element = self.wait_element_to_be_clickable(locator)
        return element.click()

    def input_text(self, locator, text):
        element = self.wait_element_to_be_visible(locator)
        element.clear()
        return element.send_keys(text)

    def current_url(self):
        return self.driver.current_url

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def wait_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(locator))

    def check_element_is_displayed(self, locator):
        return self.wait_element_to_be_visible(locator).is_displayed()

    def drag_and_drop_elements(self, first_locator, second_locator):
        start = self.wait_element_to_be_visible(first_locator)
        end = self.wait_for_element(second_locator)
        return drag_and_drop(self.driver, start, end)

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def scroll_to_element(self, locator):
        element = self.check_element_is_displayed(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)
