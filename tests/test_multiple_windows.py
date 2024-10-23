import pytest
from playwright.sync_api import Page
from pages.multiple_windows import MultipleWindows


def test_multiple_windows(context):
    if not context.pages:
        first_page = context.new_page()
    else:
        pages = context.pages
        first_page = pages[0]

    multiple_window = MultipleWindows(first_page)
    multiple_window.navigate_to_page()

    # Click the link that opens the new page
    multiple_window.new_page_link.click()

    # Wait for the new page to be added
    context.wait_for_event('page')  # waits for a new page to appear in context.pages

    # Now get the second page
    pages = context.pages  # Refresh the list of pages after the new window is opened
    second_page = pages[1]

    assert second_page.url == 'https://the-internet.herokuapp.com/windows/new'

