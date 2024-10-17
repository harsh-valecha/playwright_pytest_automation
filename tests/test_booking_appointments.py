import pytest
from playwright.sync_api import Page

from pages.book_appointment_page import BookAppointmentPage
from utils.config import Config
from pages.appoinment_page import AppointmentPage # Page Object model implemented
from pages.login_page import LoginPage

def test_page_url(page:Page):
    appointment_page = AppointmentPage(page)
    assert page.url == Config.appointment_url


def test_page_contains(page:Page):
    appointment_page = AppointmentPage(page)
    assert appointment_page.page_contains('CURA Healthcare Service')== True

@pytest.mark.parametrize("user_data",Config.get_users())
def test_login(page:Page,user_data:dict):
    appointment_page = AppointmentPage(page)
    appointment_page.make_appointment_btn.click()
    login_page = LoginPage(page)
    login_page.username_txt.fill(user_data['username'])
    login_page.password_txt.fill(user_data['password'])
    login_page.login_btn.click()
    assert page.url == Config.book_appointment_url


@pytest.mark.e2e
@pytest.mark.parametrize("form_data", Config.get_form_data())
def test_booking_appointment(page: Page, form_data: dict):
    appointment_page = AppointmentPage(page)
    appointment_page.make_appointment_btn.click()
    login_page = LoginPage(page)
    login_page.username_txt.fill(form_data['username'])
    login_page.password_txt.fill(form_data['password'])
    login_page.login_btn.click()
    assert page.url == Config.book_appointment_url
    booking_appointment_page = BookAppointmentPage(page)
    booking_appointment_page.facility_select.select_option(label=form_data['facility'])
    if form_data['apply_for_hospital_readmission']==1:
        booking_appointment_page.check_hospital_readmission.click()
    if form_data['healthcare_program']=='Medicare':
        booking_appointment_page.medicare_radio.click()
    if form_data['healthcare_program']=='Medicaid':
        booking_appointment_page.medicaid_radio.click()
    if form_data['healthcare_program'] == 'None':
        booking_appointment_page.none_radio.click()
    booking_appointment_page.visit_date_txt.fill(form_data['visit_date'])
    page.keyboard.press('Enter')
    # page.pause()
    booking_appointment_page.comment_txt.fill(form_data['comment'])
    booking_appointment_page.book_appointment_btn.click()
    assert page.url == Config.summary_url

