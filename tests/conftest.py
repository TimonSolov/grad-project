import pytest
from playwright.sync_api import sync_playwright

from pages.bank_manager_page import BankManagerAccountPage
from pages.login_page import LoginPage
from pages.customer_page import CustomerAccountPage


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page(no_viewport=True)
    page.goto(url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    yield page
    page.close()


@pytest.fixture(scope='function')
def customer_account(page):
    return CustomerAccountPage(page)


@pytest.fixture(scope='function')
def bank_manager_account(page):
    return BankManagerAccountPage(page)


@pytest.fixture(scope='function')
def bank_manager_add_customer(page):
    return BankManagerAccountPage(page)


@pytest.fixture(scope='function')
def login_page(page):
    return LoginPage(page)
