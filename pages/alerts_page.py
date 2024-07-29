from selene import browser, be, have


class AlertsPage:
    def __init__(self):
        self.browser = browser

    def open_alerts_page(self):
        self.browser.open('alerts')

    def show_alert_with_alert_button(self):
        self.browser.element('#alertButton').click()

    def switch_on_alert_and_click_close_button_on_in_alert(self):
        self.browser.driver.switch_to.alert.accept()

    def show_confirm_alert_with_two_button(self):
        self.browser.element('#confirmButton').click()

    def switch_on_confirm_alert_and_click_yes(self):
        self.browser.driver.switch_to.alert.accept()

    def wait(self):
        pass
