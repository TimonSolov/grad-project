import allure
from locators.bank_manager_login_locators import *
from pages.base_page import BasePage
from locators.login_page_locators import *


class BankManagerAccountPage(BasePage):
    @allure.step("Do login")
    def login(self):
        self.click_element(locator=BANK_MANAGER_LOGIN_BUTTON)

    @allure.step("Confirm the dialog")
    def confirm_dialog(self):
        self.page.on("dialog", lambda dialog: print(dialog.message))
        self.page.on('dialog', lambda dialog: dialog.accept())

    @allure.step("Create a new customer")
    def fill_form(self, first_name: str, last_name: str, postcode: str):
        first_name_field = self.page.wait_for_selector(selector=FIRST_NAME)
        last_name_field = self.page.wait_for_selector(selector=LAST_NAME)
        postcode_field = self.page.wait_for_selector(selector=POSTCODE_FIELD)
        first_name_field.fill(value=first_name)
        last_name_field.fill(value=last_name)
        postcode_field.fill(value=postcode)

    @allure.step("Add a new customer")
    def add_customer(self):
        self.login()
        self.click_element(ADD_CUSTOMER_TAB)
        self.fill_form(first_name='New', last_name='User', postcode='1234')
        self.click_element(locator=ADD_CUSTOMER_BUTTON)
        self.confirm_dialog()

    @allure.step("Select a customer from list")
    def select_customer(self, option: str):
        self.page.select_option(selector=CUSTOMER_SELECTOR, value=option)

    @allure.step("Select a currency from list")
    def select_currency(self, option: str):
        self.page.select_option(selector=CURRENCY_SELECTOR, value=option)

    @allure.step("Submit a form")
    def submit_form(self, locator: str):
        self.page.click(selector=locator)

    @allure.step("Delete a customer")
    def delete_customer(self, locator: str):
        self.page.click(selector=locator)
