import allure
from locators.bank_manager_login_locators import *


class TestBankManagerAccount:
    @allure.story("Bank manager login")
    def test_bank_manager_login(self, bank_manager_account):
        bank_manager_account.login()

    @allure.story("Add new customer record")
    def test_add_customer(self, bank_manager_account):
        bank_manager_account.login()
        bank_manager_account.click_element(locator=ADD_CUSTOMER_TAB)
        bank_manager_account.fill_form(first_name='New', last_name='User', postcode='1234')
        bank_manager_account.click_element(locator=ADD_CUSTOMER_BUTTON)
        bank_manager_account.confirm_dialog()
        bank_manager_account.click_element(locator=CUSTOMERS_TAB)
        assert bank_manager_account.get_text(locator=NEW_USER_FIRST_NAME) == 'New', f'Record is not found'
        assert bank_manager_account.get_text(locator=NEW_USER_LAST_NAME) == 'User', f'Record is not found'
        assert bank_manager_account.get_text(locator=NEW_USER_POSTCODE) == '1234', f'Record is not found'

    @allure.story("Assign an account to a customer")
    def test_open_account(self, bank_manager_account, bank_manager_add_customer):
        bank_manager_add_customer.add_customer()
        bank_manager_account.click_element(locator=OPEN_ACCOUNT_TAB)
        bank_manager_account.select_customer('New User')
        bank_manager_account.select_currency('Dollar')
        bank_manager_account.submit_form(locator=PROCESS_BUTTON)
        bank_manager_account.confirm_dialog()
        bank_manager_account.click_element(locator=CUSTOMERS_TAB)
        assert bank_manager_account.get_text(locator=NEW_USER_ACCOUNT_NUMBER) == "1016", f'Record is not found'

    @allure.story("Search a customer")
    def test_search_customers(self, bank_manager_account, bank_manager_add_customer):
        bank_manager_add_customer.add_customer()
        bank_manager_account.click_element(locator=CUSTOMERS_TAB)
        bank_manager_account.fill_text(locator=SEARCH_FIELD, text='Harry')
        assert bank_manager_account.get_text(locator=USER_FIRST_NAME) == 'Harry', f'Record is not found'

    @allure.story("Ascending and descending sorting by first name")
    def test_customer_sorting_by_first_name(self, bank_manager_account, bank_manager_add_customer):
        bank_manager_add_customer.add_customer()
        bank_manager_account.click_element(locator=CUSTOMERS_TAB)
        bank_manager_account.click_element(locator=FIRST_NAME_SORTING)
        assert bank_manager_account.get_text(FIRST_NAME_ON_SORTING) == 'Ron', f'Not a correct descending sorting'
        bank_manager_account.click_element(locator=FIRST_NAME_SORTING)
        assert bank_manager_account.get_text(locator=FIRST_NAME_ON_SORTING) == 'Albus', (f'Not a correct ascending '
                                                                                         f'sorting')

    @allure.story("Ascending and descending sorting by last name")
    def test_customer_sorting_by_last_name(self, bank_manager_account, bank_manager_add_customer):
        bank_manager_add_customer.add_customer()
        bank_manager_account.click_element(locator=CUSTOMERS_TAB)
        bank_manager_account.click_element(locator=LAST_NAME_ON_SORTING)
        assert bank_manager_account.get_text(locator=LAST_NAME_ON_SORTING) == 'Granger', (f'Not a correct descending '
                                                                                          f'sorting')
        bank_manager_account.click_element(locator=FIRST_NAME_SORTING)
        assert bank_manager_account.get_text(locator=LAST_NAME_ON_SORTING) == 'Weasly', (f'Not a correct ascending '
                                                                                         f'sorting')

    @allure.story("Ascending and descending sorting by postcode")
    def test_customer_sorting_by_postcode(self, bank_manager_account, bank_manager_add_customer):
        bank_manager_add_customer.add_customer()
        bank_manager_account.click_element(locator=CUSTOMERS_TAB)
        bank_manager_account.click_element(locator=POSTCODE_ON_SORTING)
        assert bank_manager_account.get_text(locator=POSTCODE_ON_SORTING) == 'E859AB', (f'Not a correct descending '
                                                                                        f'sorting')
        bank_manager_account.click_element(locator=FIRST_NAME_SORTING)
        assert bank_manager_account.get_text(POSTCODE_ON_SORTING) == 'E55555', f'Not a correct ascending sorting'

    @allure.story("Deletion of a customer record")
    def test_delete_customer(self, bank_manager_account, bank_manager_add_customer):
        bank_manager_add_customer.add_customer()
        bank_manager_account.click_element(locator=CUSTOMERS_TAB)
        bank_manager_account.fill_text(locator=SEARCH_FIELD, text='New')
        assert bank_manager_account.get_text(locator=USER_FIRST_NAME_IN_ROW) == 'New', f'User name is not found'
        bank_manager_account.delete_customer(locator=DELETE_CUSTOMER_BUTTON)
        assert bank_manager_account._is_not_visible(locator=DELETE_CUSTOMER_BUTTON), f'User name record is found'
