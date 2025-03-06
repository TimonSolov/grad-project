import allure
from locators.bank_manager_login_locators import *
from locators.customer_login_page_locators import *


class TestLoginUsers:
    @allure.story("Customer user account login operation")
    def test_customer_login(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        assert customer_account.get_text(locator=TRANSACTION_TAB) == "Transactions", f'There was no successful login'

    @allure.story("Bank manager user account login operation")
    def test_bank_manager_login(self, bank_manager_account):
        bank_manager_account.login()
        assert bank_manager_account.get_text(locator=ADD_CUSTOMER_TAB) == "Add Customer", (f'There was no successful '
                                                                                           f'login')
