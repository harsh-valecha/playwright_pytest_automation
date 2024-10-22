import pytest
from playwright.sync_api import Page,TimeoutError
from utils.config import Config

class DynamicPage:
    def __init__(self,page:Page):
        self.page = page
        self.start_btn = page.locator(selector='div#start button')
        self.hidden_element_selector = 'div#finish h4'


    def navigate_to_url(self,url=Config.dynamic_element_url):
        self.page.goto(url)


    def get_dynamic_element_text(self):
        element = self.page.wait_for_selector(self.hidden_element_selector,timeout=7000)
        try :
            if element:
                return element.text_content()
        except TimeoutError:
            print("Element not found within the specified time.")
