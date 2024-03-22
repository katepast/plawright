from pytest_playwright.pytest_playwright import page


class HomePage:
    def __init__(self, page):
        self.page = page
        self.whats_new_title = page.locator("text=What's new")
        self.heading_title = page.locator('xpath=//*[@id="page-title-heading"]/span')
        self.sign_in_btn = page.get_by_role("link", name="Sign In")

    def click_whats_new_title(self):
        self.whats_new_title.click()

    def click_sign_in_btn(self):
        self.sign_in_btn.click()
