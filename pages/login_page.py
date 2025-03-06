from locators.login_page_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self):
        self.click_element(locator=CUSTOMER_LOGIN_BUTTON)
