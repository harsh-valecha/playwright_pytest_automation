import pytest
from playwright.sync_api import Page
from utils.config import Config

class BookAppointmentPage:
    def __init__(self,page:Page,url=Config.book_appointment_url):
        self.page = page
        self.page.goto(Config.book_appointment_url)
        self.facility_select = page.locator("#combo_facility")
        self.check_hospital_readmission = page.locator("#chk_hospotal_readmission")
        self.medicare_radio = page.locator("#radio_program_medicare")
        self.medicaid_radio = page.locator("#radio_program_medicaid")
        self.none_radio = page.locator("#radio_program_none")
        self.visit_date_txt = page.locator("#txt_visit_date")
        self.comment_txt = page.locator("#txt_comment")
        self.book_appointment_btn = page.locator("#btn-book-appointment")