from playwright.sync_api import Playwright,expect
import pytest
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage
from utils.read_jsondata import read_json_data

test_data=read_json_data("data/login_testdata.json")

@pytest.mark.parametrize("user_data",test_data)
def test_search_product(playwright:Playwright,browser_context,user_data):
    page= browser_context.new_page()
    page.goto("http://automationexercise.com")
    loginpage=LoginPage(page)
    searchpage=SearchPage(page)
    loginpage.click_login_link()
    loginpage.fill_login_form(
        email=user_data["email"],
        password=user_data["password"]
    )
    searchpage.navigate_to_products_page()
    searchpage.verify_all_products_header()
    searchpage.search_product("Blue Top")
    searchpage.verify_search_results("Blue Top")


