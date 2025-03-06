import allure
from locators.customer_login_page_locators import *
from pages.base_page import BasePage
from locators.login_page_locators import *


class CustomerAccountPage(BasePage):

    @allure.step("Do login by a customer")
    def click_customer_option(self):
        self.click_element(CUSTOMER_LOGIN_BUTTON)

    @allure.step("Do customer login")
    def click_customer_to_login(self):
        self.click_element(CUSTOMER_ACCEPT_TO_LOGIN_BUTTON)

    @allure.step("Check whether a customer name is visible or not")
    def is_customer_name(self):
        self.is_visible(CUSTOMER_NAME)

    @allure.step("Particular customer login")
    def customer_login(self, option: str):
        self.click_customer_option()
        self.select_username(option)
        self.click_customer_to_login()

    @allure.step("Customer logout")
    def customer_logout(self):
        self.click_element(locator=CUSTOMER_LOGOUT_BUTTON)

    @allure.step("Make a deposit operation")
    def input_deposit(self, value: str):
        self.page.fill(selector=DEPOSIT_INPUT_FIELD, value=value)
        self.page.click(DEPOSIT_SUBMIT_BUTTON)

    @allure.step("Check current customer balance")
    def actual_balance(self):
        self.page.wait_for_selector(CURRENT_BALANCE_LOCATOR)
        self.get_text(CURRENT_BALANCE_LOCATOR)

    @allure.step("Make a withdrawal")
    def do_withdrawal(self, value: str):
        self.click_element(WITHDRAWAL_TAB)
        self.page.fill(selector=WITHDRAWAL_AMOUNT, value=value)
        self.click_element(WITHDRAWAL_SUBMIT_BUTTON)

    @allure.step("Return on previous tab(page)")
    def transactions_back(self):
        self.click_element(TRANSACTION_BACK_BUTTON)

    @allure.step("Refresh a tab")
    def refresh_transactions_list(self):
        self.click_element(TRANSACTION_TAB)
        self.transactions_back()
        self.click_element(TRANSACTION_TAB)
        self.transactions_back()
        self.click_element(TRANSACTION_TAB)
        self.transactions_back()

    @allure.step("Select an account")
    def select_account(self, option: str):
        self.click_element(ACCOUNT_NUMBER_LOCATOR)
        self.page.select_option(selector=ACCOUNT_NUMBER_LOCATOR, value=option)

    @allure.step("Make transactions reset")
    def reset_transactions(self):
        self.click_element(TRANSACTION_RESET)
