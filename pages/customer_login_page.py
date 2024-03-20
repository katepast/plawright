
class CustomerLoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.get_by_label("Email", exact=True)
        self.password_input = page.get_by_label("Password")
        self.sign_in_btn = page.get_by_role("button", name="Sign In")

    def set_email(self, value):
        self.email_input.fill(value)

    def set_password(self, value):
        self.password_input.fill(value)

    def click_sign_in(self):
        self.sign_in_btn.click()

