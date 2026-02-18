import playwright
import pytest
from playwright.sync_api import Playwright
@pytest.fixture(scope="session")
def browser_context(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()