import pytest
from playwright.sync_api import Page
from utils.config import Config

class AppointmentPage:
    def __init__(self,page:Page,url=Config.appointment_url):
        self.page = page
        self.page.goto(url)
        self.make_appointment_btn = page.locator("//a[@id='btn-make-appointment']") # provided xpath


    def page_contains(self,value:str):
        return value in self.page.content()

