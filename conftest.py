import os

import os
import pytest
from playwright.sync_api import Playwright
from pages.customer_login_page import CustomerLoginPage
from pages.home_page import HomePage

from pages.customer_login_page import CustomerLoginPage
from pages.home_page import HomePage
from utils.url import HOME_PAGE_URL

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['EMAIL']


@pytest.fixture()
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    browser = playwright.chromium.launch(headless=True,slow_mo=500)
    context = browser.new_context()
    # Open new page and go to our URL
    page = context.new_page()
    page.goto(HOME_PAGE_URL)
    yield page
    # Teardown: Close the browser context
    browser.close()


@pytest.fixture()
def sign_in(set_up):
    page = set_up
    home_page = HomePage(page)
    cust_page = CustomerLoginPage(page)
    home_page.click_sign_in_btn()
    cust_page.set_email(EMAIL)
    cust_page.set_password(PASSWORD)
    yield page

