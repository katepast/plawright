import re
from playwright.sync_api import expect
from pages.customer_login_page import CustomerLoginPage
from pages.home_page import HomePage


def test_open_whats_new_page(set_up):
    page = set_up
    home_page = HomePage(page)
    home_page.click_whats_new_title()
    act_res = home_page.heading_title.text_content()
    assert act_res == "What's New", 'Whats New title is absent on the page'
    expect(page).to_have_url(re.compile(".*/what-is-new.html"))


def test_sign_in(set_up):
    page = set_up
    home_page = HomePage(page)
    cust_page = CustomerLoginPage(page)
    home_page.click_sign_in_btn()
    cust_page.set_email("test@gmail.com")
    cust_page.set_password("test123456")
    cust_page.click_sign_in()
    page.set_default_timeout(3000)
    expect(page.get_by_role("alert")).to_contain_text(timeout=800, expected='The account sign-in was incorrect')
    
