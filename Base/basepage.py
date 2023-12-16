from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Base.elements import Elements
from commons import constants


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.elements = Elements()

    def wait_and_get_element(self, element_locator, by=By.CSS_SELECTOR, time_out=10):
        """Waits for an element to be present and returns it."""
        element = WebDriverWait(self.driver, time_out).until(
            expected_conditions.presence_of_element_located((by, element_locator))
        )
        if not element:
            raise Exception(constants.ELEMENT_NOT_FOUND.format(element_locator, None))
        return element

    def compare_and_assert(self, element_id, expected):
        """Compares the actual text of an element with the expected text and raises an assertion error if they don't match."""
        actual = self.wait_and_get_element(element_id).text
        assert expected == actual or actual in expected, constants.VALUES_NOT_MATCHED.format(actual, expected)

