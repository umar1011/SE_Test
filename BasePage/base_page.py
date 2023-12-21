from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Basepage.elements import Elements
from commons import constants


class BasePage:
    """
    Base page for all available screens
    """

    def __init__(self, driver):
        self.driver = driver
        self.elements = Elements()

    def wait_and_get_element(self, element_locator, by=By.CSS_SELECTOR, time_out=10):
        return WebDriverWait(self.driver, time_out).until(
            expected_conditions.presence_of_element_located((by, element_locator))
        )

    def compare_actual_and_expected_result(self, element_id, actual):
        element = self.wait_and_get_element(element_id)
        expected = element.text

        if expected == actual or actual in expected:
            return True
        raise Exception(constants.VALUES_NOT_MATCHED.format(actual, expected))

    @staticmethod
    def format_error_message(actual, expected):
        return constants.VALUES_NOT_MATCHED.format(actual, expected)

    def check_element_text_contains(self, element_id, expected_text):
        element = self.wait_and_get_element(element_id)
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(element, expected_text)
        )

