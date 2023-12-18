from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from Base.elements import Elements
from commons import constants


class BasePage:
    """
     Base page for all available screens
    """

    def __init__(self, driver):
        self.driver = driver
        self.elements = Elements()

    def wait_and_get_element(self, element_locator, by=By.CSS_SELECTOR, time_out=10):

        """
        wait and get element from the screen, block until given time out
        :param element_locator: (str) element locator
        :param by: Element Selector types
        :param time_out: (int) defaults to 5 sec
        
        :return: (WebElement) target_element
        """

        element = WebDriverWait(self.driver, time_out).until(
                expected_conditions.presence_of_element_located((by, element_locator)))

        if not element:
            raise Exception(constants.ELEMENT_NOT_FOUND.format(element_locator, None))
        return element

    def compare_actual_and_expected_result(self, element_id, actual):
        expected = self.wait_and_get_element(element_id).text
        if expected == actual or actual in expected:
            return True
        raise Exception(constants.VALUES_NOT_MATCHED.format(actual, expected))