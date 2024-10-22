import pytest
from playwright.sync_api import Page,TimeoutError
from utils.config import Config

class JQueryDynamicPage:
    def __init__(self,page:Page):
        self.page = page
        self.enabled_menu = page.locator("//li[@id='ui-id-3']/span")
        self.downloads_menu = page.locator("//li[@id='ui-id-4']/span")
        self.excel_link = page.locator("//a[text()='Excel']")

    def navigate_to_url(self,url=Config.jquery_ui_url):
        self.page.goto(url)