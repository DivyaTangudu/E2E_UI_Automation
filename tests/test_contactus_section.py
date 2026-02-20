from playwright.sync_api import Playwright
from pages.ContactPage import ContactUsPage

def test_contact_us_section(playwright:Playwright,browser_context):
    page=browser_context.new_page()
    page.goto("http://automationexercise.com")
    contactpage=ContactUsPage(page)
    
    contactpage.click_contact_us()
    contactpage.verify_contact_us_header()    
    contactpage.fill_contact_form(
        name="Test User",
        email="testuser@example.com",
        subject="Test Subject",
        message="This is a test message.",
        file_path="E:\\hello.txt"
    )