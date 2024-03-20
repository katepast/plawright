import pytest
from playwright.sync_api import Playwright
from utils.url import HOME_PAGE_URL


@pytest.fixture()
def set_up(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True,slow_mo=500)
    context = browser.new_context()
    # Open new page and go to our URL
    page = context.new_page()
    page.goto(HOME_PAGE_URL)
    yield page
    # Teardown: Close the browser context
    browser.close()


