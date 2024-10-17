import pytest
from playwright.sync_api import Page
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
def test_book_appointment(page:Page,user_data:dict):
    appointment_page = AppointmentPage(page)
    appointment_page.make_appointment_btn.click()
    login_page = LoginPage(page)
    login_page.username_txt.fill(user_data['username'])
    login_page.password_txt.fill(user_data['password'])
    login_page.login_btn.click()
    assert page.url == Config.book_appointment_url