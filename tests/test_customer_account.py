import allure
from locators.customer_login_page_locators import *
from locators.login_page_locators import *


class TestCustomerAccount:
    @allure.story("Customer deposit operation")
    def test_deposit_operation(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        customer_account.click_element(locator=CUSTOMER_DEPOSIT_TAB)
        customer_account.input_deposit('200')
        assert customer_account.get_text(
            locator=ERROR_NOTIFICATION) == "Deposit Successful", f'Not found or wrong operation executed'
        customer_account.refresh_transactions_list()
        customer_account.click_element(locator=TRANSACTION_TAB)
        customer_account.get_text(locator=TRANSACTION_AMOUNT)
        assert customer_account.get_text(locator=TRANSACTION_AMOUNT) == '200', f'Not found or wrong amount'

    @allure.story("Customer deposit transaction existence")
    def test_deposit_transaction(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        customer_account.click_element(locator=CUSTOMER_DEPOSIT_TAB)
        customer_account.input_deposit('200')
        assert customer_account.get_text(
            locator=ERROR_NOTIFICATION) == "Deposit Successful", f'Not found or wrong operation executed'
        customer_account.refresh_transactions_list()
        customer_account.click_element(locator=TRANSACTION_TAB)
        assert customer_account.get_text(locator=TRANSACTION_AMOUNT) == '200', f'Not found or wrong amount'

    @allure.story("Customer withdrawal operation")
    def test_withdrawal_operation(self, page, customer_account):
        customer_account.customer_login(option="Harry Potter")
        customer_account.click_element(locator=CUSTOMER_DEPOSIT_TAB)
        customer_account.input_deposit('200')
        assert customer_account.get_text(
            locator=ERROR_NOTIFICATION) == "Deposit Successful", f'Not found or wrong operation executed'
        # necessary steps to update DOM
        customer_account.refresh_transactions_list()
        customer_account.click_element(locator=TRANSACTION_TAB)
        customer_account.transactions_back()
        # end of necessary steps
        customer_account.do_withdrawal('200')
        assert customer_account.get_text(
            locator=WITHDRAWAL_NOTIFICATION) == "Transaction successful", f'Not found or wrong operation executed'

    @allure.story("Customer withdrawal transaction")
    def test_withdrawal_transaction(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        customer_account.click_element(locator=CUSTOMER_DEPOSIT_TAB)
        customer_account.input_deposit('200')
        assert customer_account.get_text(
            ERROR_NOTIFICATION) == "Deposit Successful", f'Not found or wrong operation executed'
        customer_account.refresh_transactions_list()
        customer_account.do_withdrawal('200')
        customer_account.refresh_transactions_list()
        customer_account.click_element(locator=TRANSACTION_TAB)
        assert customer_account.get_text(locator=TRANSACTION_TYPE_DEBIT) == 'Debit', (f'Not found or wrong operation '
                                                                                      f'executed')

    @allure.story("Customer accounts selection")
    def test_select_accounts(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        assert customer_account.get_text(locator=ACCOUNT1_SELECTED_NUMBER_LOCATOR) == '1004 ', f'Wrong account selected'
        customer_account.select_account('1005')
        assert customer_account.get_text(locator=ACCOUNT2_SELECTED_NUMBER_LOCATOR) == '1005 ', f'Wrong account selected'
        customer_account.select_account('1006')
        assert customer_account.get_text(locator=ACCOUNT3_SELECTED_NUMBER_LOCATOR) == '1006 ', f'Wrong account selected'
        customer_account.select_account('1004')
        assert customer_account.get_text(locator=ACCOUNT1_SELECTED_NUMBER_LOCATOR) == '1004 ', f'Wrong account selected'

    @allure.story("Return to homepage")
    def test_home_page(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        customer_account.click_element(locator=HOME_BUTTON)
        assert customer_account.get_text(locator=CUSTOMER_LOGIN_BUTTON) == "Customer Login", f'It is not a home page'
        assert customer_account.get_text(locator=BANK_MANAGER_LOGIN_BUTTON) == "Bank Manager Login", (f'It is not a '
                                                                                                      f'home page')

    @allure.story("Reset of customer transactions")
    def test_reset_transactions_list(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        customer_account.go_on(locator=CUSTOMER_DEPOSIT_TAB)
        customer_account.input_deposit('200')
        assert customer_account.get_text(
            locator=ERROR_NOTIFICATION) == "Deposit Successful", f'Not found or wrong operation executed'
        customer_account.refresh_transactions_list()
        customer_account.go_on(locator=TRANSACTION_TAB)
        assert customer_account.get_text(locator=TRANSACTION_AMOUNT) == '200', f'Not found or wrong amount'
        customer_account.transactions_back()
        customer_account.do_withdrawal('200')
        customer_account.refresh_transactions_list()
        customer_account.go_on(locator=TRANSACTION_TAB)
        assert customer_account.get_text(locator=TRANSACTION_TYPE_DEBIT) == 'Debit', (f'Not found or wrong operation '
                                                                                      f'executed')
        customer_account.reset_transactions()
        customer_account.transactions_back()
        customer_account.refresh_transactions_list()
        customer_account.go_on(locator=TRANSACTION_TAB)
        assert customer_account._is_not_visible(locator=TRANSACTION_RESET), f'Not found or wrong amount'

    @allure.story("Customer logout")
    def test_customer_logout(self, customer_account):
        customer_account.customer_login(option="Harry Potter")
        customer_account.customer_logout()
        assert customer_account.get_text(locator=HOME_LOGO) == "XYZ Bank", f'There was no successful logout'
