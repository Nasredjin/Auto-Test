import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

def test_user_login(page):
    page.goto("https://example.com/login")  # замените на реальный URL
    page.fill("#username", "test_user")
    page.fill("#password", "secure_password")
    page.click("#login_button")
    page.wait_for_selector("#dashboard")  # Проверяем, что логин успешен