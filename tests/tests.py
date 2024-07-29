import selene

from pages.sample_app_page import SampleAppPage
from pages.text_input import TextInputPage
from pages.alerts_page import AlertsPage


def test_sampleapp_log_in_test(browser_manager):
    page = SampleAppPage()
    page.open_sampleapp_page()
    page.fill_user_and_password_fields(user = 'Tester', password = 'pwd')
    page.log_in_button_click()
    page.check_message_text('Welcome, Tester!')


def test_sampleapp_submit_form_without_requiered_fields(browser_manager):
    page = SampleAppPage()
    page.open_sampleapp_page()
    page.log_in_button_click()
    page.check_message_text('Invalid username/password')


def test_sampleapp_logout_test(browser_manager):
    page = SampleAppPage()
    page.open_sampleapp_page()
    page.fill_user_and_password_fields(user = 'Tester', password = 'pwd')
    page.log_in_button_click()
    page.log_out_button_click()
    page.check_message_text('User logged out.')


def test_update_button_name(browser_manager):
    page = TextInputPage()
    page.open_textinput_page()
    page.fill_new_button_name_field("New name")
    page.submit_new_button_name()
    page.check_new_name_of_button("New name")


def test_alert_close_alert():
    page = AlertsPage()
    page.open_alerts_page()
    page.show_alert_with_alert_button()
    page.switch_on_alert_and_click_close_button_on_in_alert()

def test_alert_with_two_buttons_confirm_alert():
    page = AlertsPage()
    page.open_alerts_page()
    page.show_confirm_alert_with_two_button()
    page.switch_on_confirm_alert_and_click_yes()
    # page.switch_on_alert_and_click_close_button_on_in_alert()
