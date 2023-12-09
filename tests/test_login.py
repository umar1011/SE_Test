import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_login_with_valid_credentials(browser, username, password):
    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    # Assert successful login (e.g., check URL, element presence)
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize("username, password", [("userwrong", "secret_sauce"), ("valid_username", "invalid_password")])
def test_login_with_invalid_credentials(browser, username, password):
    login_page = LoginPage(browser)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # Assert error message displayed
    assert "Epic sadface: Username and password do not match any user in this service"