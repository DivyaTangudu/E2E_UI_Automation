from playwright.sync_api import Playwright,expect
import pytest
from pages.LoginPage import LoginPage
from utils.read_jsondata import read_json_data

# Read JSON data
test_data = read_json_data("data/login_testdata.json")    

@pytest.mark.parametrize("user_data",test_data)
def test_login(playwright:Playwright,browser_context,user_data):
    page = browser_context.new_page()
    page.goto("http://automationexercise.com")
    login=LoginPage(page)
    login.click_login_link()    
    login.verify_login_header()
    login.fill_login_form(
        email=user_data["email"],
        password=user_data["password"])
    # Add assertions to verify successful login, e.g., check for user profile visibility
    expect(login.userlogintext()).to_be_visible()
    login.verify_user_logout()

    