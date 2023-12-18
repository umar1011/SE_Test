"""Application Login Page"""
from Base.basepage import BasePage
from commons import constants


class Login(BasePage):
    """
    Class for handling Login Page
    """

    def email_id_field(self):
        """
        get email if field
        """
        return self.wait_and_get_element(self.elements.USER_NAME_CSS)

    def password_field(self):
        """
        get password field
        """
        return self.wait_and_get_element(self.elements.PASSWORD_CSS)

    def get_login_button(self):
        return self.wait_and_get_element(self.elements.LOGIN_BUTTON_CSS)

    def validate_error_message(self, value_to_match):
        """
        check error message and save it
        :return: (bool) True if error message appears and match with the one we provided
        """
        return self.compare_actual_and_expected_result(self.elements.ERROR_MESSAGE_CSS, value_to_match)

    def verify_dashboard_is_loaded(self, value_to_match=constants.title_value):
        """
        check title must match with value provided
        :return: (bool) True if value matched

        """
        return self.compare_actual_and_expected_result(self.elements.DASHBOARD_TITLE_CSS, value_to_match)

    def login(self, user_name=constants.EMAIL_ID, password=constants.PASSWORD):
        self.email_id_field().send_keys(user_name)
        self.password_field().send_keys(password)
        self.get_login_button().click()
