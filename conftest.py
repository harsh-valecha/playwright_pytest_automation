import pytest
from playwright.sync_api import sync_playwright
import os
import allure

# Directory to store failed test screenshots
FAILED_SCREENSHOTS_DIR = "failed_test_screenshots/"

# fixture for controlling the context
@pytest.fixture(scope="function")
def context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


# Fixture to start and close Playwright browser and pass the page object
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()  # Close the page after the test



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute the test and get the report
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == 'call' and report.failed:
        # Get the Playwright page object from the test's arguments
        page = item.funcargs.get('page')
        if page:
            # Define the screenshot directory and create it if necessary
            os.makedirs(FAILED_SCREENSHOTS_DIR, exist_ok=True)

            # Generate a unique screenshot path based on the test's node id
            screenshot_path = os.path.join(FAILED_SCREENSHOTS_DIR, f"{item.nodeid.replace('::', '_')}.png")

            # Capture the full page screenshot
            page.screenshot(path=screenshot_path, full_page=True)

            # Attach the screenshot to the Allure report
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
