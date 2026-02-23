from playwright.sync_api import Playwright,expect
from pages.ProductsDetailsPage import ProductDetailsPage

def test_product_details(playwright:Playwright,browser_context):
    page=browser_context.new_page()
    page.goto("http://automationexercise.com")
    product_details=ProductDetailsPage(page)
    
    product_details.navigate_to_products_page()
    product_details.verify_product_details_header()
    product_details.close_google_vignette()
    product_name="Blue Top"
    expected_details={
        "name": "Blue Top",
        "category ": "Category: Women",
        "price": "Rs. 500",
        "availability": "Availability: In Stock",
        "condition": "Condition: New",
        "brand": "Brand: Polo"
    }
    product_details.click_view_product(product_name)
    product_details.verify_product_details(expected_details)
    