import pytest
from playwright.sync_api import Page
from utils.config import Config


class LoginPage:
    def __init__(self,page:Page,url = Config.login_url):
        self.page = page
        self.page.goto(Config.login_url)
        self.username_txt = page.locator('#txt-username') # using css selector
        self.password_txt = page.locator('#txt-password')
        self.login_btn = page.locator('#btn-login')
