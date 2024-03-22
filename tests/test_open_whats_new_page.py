import re
import pytest
from playwright.sync_api import expect

from pages.customer_login_page import CustomerLoginPage
from pages.home_page import HomePage


@pytest.mark.smoke
def test_open_whats_new_page(set_up):
    page = set_up
    home_page = HomePage(page)
    home_page.click_whats_new_title()

    act_res = home_page.heading_title.text_content()
    assert act_res == "What's New", 'Whats New title is absent on the page'
    expect(page).to_have_url(re.compile(".*/what-is-new.html"))


@pytest.mark.smoke
def test_sign_in(sign_in):
    page = sign_in
    cust_page = CustomerLoginPage(page)
    cust_page.click_sign_in()
    #expect(page.get_by_text("Customer Login")).to_be_visible()
    expect(page).to_have_url(re.compile(".*/customer/account/login/*"))