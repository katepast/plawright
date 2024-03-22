import re
from playwright.sync_api import expect
from pages.customer_login_page import CustomerLoginPage
from pages.home_page import HomePage
import pytest
import os


@pytest.mark.smoke
def test_open_whats_new_page(set_up):
    page = set_up
    home_page = HomePage(page)
    home_page.click_whats_new_title()
    act_res = home_page.heading_title.text_content()
    assert act_res == "What's New", 'Whats New title is absent on the page'
    expect(page).to_have_url(re.compile(".*/what-is-new.html"))


@pytest.mark.smoke
def test_sign_in(set_up):
    page = set_up
    home_page = HomePage(page)
    cust_page = CustomerLoginPage(page)
    home_page.click_sign_in_btn()
    cust_page.set_email(os.environ['EMAIL'])
    cust_page.set_password(os.environ['PASSWORD'])
    cust_page.click_sign_in()
    expect(page.get_by_text('The account sign-in was incorrect')).to_be_visible()
