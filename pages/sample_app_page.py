from selene.support.shared import browser
from selene import have


class SampleAppPage:
    def __init__(self):
        self.browser = browser

    def open_sampleapp_page(self):
        self.browser.open('sampleapp')

    def fill_user_and_password_fields(self, user, password):
        self.browser.element("input[name='UserName']").send_keys(user)
        self.browser.element("input[name='Password']").send_keys(password)

    def log_in_button_click(self):
        self.browser.element('#login').click()

    def log_out_button_click(self):
        self.browser.element("//button[text()='Log Out']").click()

    def check_message_text(self, expected_text):
        self.browser.element('#loginstatus').should(have.text(expected_text))
