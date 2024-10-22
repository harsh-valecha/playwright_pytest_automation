import pytest
from playwright.sync_api import Page
from pages.dynamic_page import DynamicPage
from pages.jqueryui import JQueryDynamicPage

def test_dynamic_element(page):
    dynamic_page = DynamicPage(page)
    dynamic_page.navigate_to_url()
    dynamic_page.start_btn.click()
    assert dynamic_page.get_dynamic_element_text()=='Hello World!'

def test_jqueryui_elements(page):
    jqueryui_page = JQueryDynamicPage(page)
    jqueryui_page.navigate_to_url()
    jqueryui_page.enabled_menu.hover(force=True)
    page.wait_for_timeout(2000)
    assert jqueryui_page.downloads_menu.is_visible()==True
    jqueryui_page.downloads_menu.hover(force=True)
    page.wait_for_timeout(2000)
    assert jqueryui_page.excel_link.is_visible()==True
