import allure
from playwright.sync_api import Page
from locators.customer_login_page_locators import *


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open the site URL")
    def open_url(self, url: str):
        self.page.goto(url=url)

    @allure.step("Click a web element")
    def click_element(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        element.click()

    @allure.step("Navigate to")
    def go_on(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        element.click()

    @allure.step("Type a text")
    def fill_text(self, locator: str, text: str):
        element = self.page.wait_for_selector(selector=locator)
        element.fill(value=text)

    @allure.step("Get a text from an element")
    def get_text(self, locator: str) -> str:
        element = self.page.wait_for_selector(selector=locator)
        return element.inner_text()

    @allure.step("Check the element is visible")
    def is_visible(self, locator: str) -> bool:
        is_element = self.page.is_visible(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Element is not displayed on page.')

    @allure.step("Check that element is not visible")
    def _is_not_visible(self, locator: str) -> bool:
        is_element = self.page.is_visible(selector=locator)
        if not is_element:
            return True
        else:
            raise Exception('Element is displayed on page.')

    @allure.step("Check whether the element is clickable")
    def is_clickable(self, locator: str) -> bool:
        is_element = self.page.is_enabled(selector=locator)
        if is_element:
            return True
        else:
            raise Exception("Element is not clickable.")

    @allure.step("Check whether an element is inactive")
    def __is_inactive(self, locator: str):
        self.page.is_disabled(selector=locator)

    @allure.step("Select an option from a drop-down list")
    def select_username(self, option: str):
        self.click_element(locator=USER_NAME)
        self.page.select_option(selector=USER_NAME, value=option)
