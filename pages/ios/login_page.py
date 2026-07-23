from pages.ios.base_page import BasePage
from locators.ios.login_locator import LoginLocator


class LoginPage(BasePage):

    def login(self, username, password):
        self.type(LoginLocator.USERNAME, username)
        self.type(LoginLocator.PASSWORD, password)
        self.click(LoginLocator.LOGIN_BUTTON)

    def is_login_success(self):
        return self.is_displayed(LoginLocator.PRODUCTS_TITLE)