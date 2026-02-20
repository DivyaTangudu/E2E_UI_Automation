from playwright.sync_api import Playwright,expect
import pytest
from pages.LoginPage import LoginPage
from utils.read_jsondata import read_json_data

test_data=read_json_data("data/incorrect_logindata.json")

@pytest.mark.parametrize("user_data",test_data)
def test_incorrect_login(playwright:Playwright,browser_context,user_data):
    page = browser_context.new_page()
    page.goto("http://automationexercise.com")
    login=LoginPage(page)
    login.click_login_link()
    login.verify_login_header()
    login.fill_login_form(user_data["email"],user_data["password"])
    login.verify_error_message()