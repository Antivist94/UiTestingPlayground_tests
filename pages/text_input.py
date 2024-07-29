from selene import browser, be, have


class TextInputPage:
    def __init__(self):
        self.browser = browser

    def open_textinput_page(self):
        self.browser.open('textinput')

    def fill_new_button_name_field(self,value):
        self.browser.element('#newButtonName').should(be.blank).send_keys(value)

    def submit_new_button_name(self):
        self.browser.element('#updatingButton').click()

    def check_new_name_of_button(self,value):
        self.browser.element('#updatingButton').should(have.text(value))