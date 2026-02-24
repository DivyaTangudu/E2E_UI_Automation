from playwright.sync_api import Playwright,expect
import pytest
from pages.LoginPage import LoginPage
from pages.SearchPage import SearchPage
from pages.PlaceorderPage import PlaceorderPage
from utils.read_jsondata import read_json_data

test_data=read_json_data("data/login_testdata.json")

@pytest.mark.parametrize("user_data",test_data)
def test_place_order(playwright:Playwright,browser_context,user_data):
    page = browser_context.new_page()
    page.goto("http://automationexercise.com")
    
    #Login
    login=LoginPage(page)
    login.click_login_link()
    login.fill_login_form(user_data["email"],user_data["password"])


    #Search for product
    searchpage=SearchPage(page)
    searchpage.navigate_to_products_page()
    searchpage.search_product("Blue Top")
    
    #Add to cart
    placeorder=PlaceorderPage(page)
    page.wait_for_timeout(2000)  # Wait for the cart modal to appear
    placeorder.add_product_to_cart()
    
    #View cart and proceed to checkout
    placeorder.view_cart()
    placeorder.proceed_to_checkout()
    
    #Fill payment details and place order
    placeorder.fill_payment_details("divya","4111111111111111","123","12","2025")
    placeorder.place_order()
    