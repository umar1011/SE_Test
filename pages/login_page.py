from asyncio import constants
from selenium.webdriver.common.by import By
from BasePage.elements import Elements 
from BasePage.base_page import BasePage
from commons.constants import VALUES_NOT_MATCHED

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def email_id_field(self):
        return self.wait_and_get_element(self.elements.USER_NAME_CSS)
    
    def password_field(self):
        return self.wait_and_get_element(self.elements.PASSWORD_CSS)

    def login_button(self):
        return self.wait_and_get_element(self.elements.LOGIN_BUTTON_CSS)
    
    def valid_error_message(self, value_to_match):
        return self.compare_actual_and_expected_result(self.elements.ERROR_MESSAGE_CSS, value_to_match)
    
    def verify_dashboard_is_loaded(self, value_to_match=constants.title_value):
        return self.compare_actual_and_expected_result(self.elements.DASHBOARD_TITLE_CSS, value_to_match)
    
    def login(self, user_name = constants.EMAIL_ID, password=constants.PASSWORD):
        self.email_id_field().send_keys(user_name)
        self.password_field().send_keys(password)
        self.login_button().click()