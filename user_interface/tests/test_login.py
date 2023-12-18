"""Check All Login Test Scenarios"""
from user_interface.pages.login_page import Login
import pytest
import logging
from commons import constants


class TestLogin:

    def test_login_with_valid_credentials(self, driver):
        """
        Go to Browser
        Launch Application
            Login Screen Appears

        Enter Valid username and Password
        Hit Login Button
            Dashboard is loaded successfully

        """
        main_page = Login(driver)
        main_page.login()
        assert main_page.verify_dashboard_is_loaded()
        logging.info("User is successfully Logged in")

    def test_login_with_invalid_password(self, driver):
        """
        Go to Browser
        Launch Application
            Login Screen Appears

        Enter Valid Email Id and invalid Password

        Hit Login Button
            error message appears and value error value must match with the one we provided

        """
        main_page = Login(driver)
        main_page.login(password="test")
        assert main_page.validate_error_message(value_to_match=constants.error_message)
        logging.info(f"error message appears and value error value must match with: {constants.error_message}")

    def test_login_with_invalid_username(self, driver):
        """
        Go to Browser
        Launch Application
            Login Screen Appears

        Enter inValid username and valid Password

        Hit Login Button
            error message appears and value error value must match with the one we provided

        """
        main_page = Login(driver)
        main_page.login(user_name="test")
        assert main_page.validate_error_message(value_to_match=constants.error_message)
        logging.info(f"error message appears and value error value must match with: {constants.error_message}")

    def test_login_without_credentials(self, driver):
        """
        Go to Browser
        Launch Application
            Login Screen Appears

        Enter inValid username and valid Password

        Hit Login Button
            error message appears and value error value must match with the one we provided : (Username is required)

        """
        main_page = Login(driver)
        main_page.login(user_name="", password="")
        assert main_page.validate_error_message(value_to_match=constants.user_name_required_error_message)
        logging.info(f"error message appears and value error value must match with:"
                     f" {constants.user_name_required_error_message}")