import pytest
from playwright.sync_api import Page
from utils.config import Config


class MultipleWindows:
    def __init__(self,page:Page):
        self.page = page
        self.new_page_link = page.get_by_text('Click Here')

    def navigate_to_page(self,url = Config.multiple_windows_url):
        self.page.goto(url)