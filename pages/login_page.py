from selenium.webdriver.common.by import By
from BasePage.elements import Elements 

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # Page elements using locators
        self.username_field = (By.CSS_SELECTOR, Elements.USER_NAME_CSS)
        self.password_field = (By.CSS_SELECTOR, Elements.PASSWORD_CSS)
        self.login_button = (By.CSS_SELECTOR, Elements.LOGIN_BUTTON_CSS)

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
