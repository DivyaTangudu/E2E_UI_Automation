from playwright.sync_api import Playwright,expect

class ProductDetailsPage:
    def __init__(self,page:Playwright):
        self.page=page
        self.productspage_link=self.page.get_by_role(role="link",name="Products")
        self.product_details_header=self.page.locator("h2", has_text="Product Details")
        self.product_list=self.page.locator(".features_items .col-sm-4")
        self.view_product_button=lambda product_name: self.page.locator(".features_items .col-sm-4", has_text=product_name).get_by_role("button", name="View Product")
        self.product_name=self.page.locator(".product-information h2")
        self.product_category=self.page.locator(".product-information p", has_text="Category")
        self.product_price=self.page.locator(".product-information span")   
        self.product_availability=self.page.locator(".product-information p", has_text="Availability")
        self.product_condition=self.page.locator(".product-information p", has_text="Condition")    
        self.product_brand=self.page.locator(".product-information p", has_text="Brand")

    def navigate_to_products_page(self):
        self.productspage_link.click()
        #self.page.go_back()  # Navigate back to the previous page to ensure we are on the products page

    def verify_product_details_header(self):
        print(self.product_details_header.inner_text())
        assert self.product_details_header.is_visible(),"Product details header is not visible"
    
    def click_view_product(self,product_name):
        self.view_product_button(product_name).click()

    def verify_product_details(self,expected_details):
        assert self.product_name.inner_text() == expected_details["name"], f"Expected product name '{expected_details['name']}' but got '{self.product_name.inner_text()}'"
        assert self.product_category.inner_text().endswith(expected_details["category"]), f"Expected category to end with '{expected_details['category']}' but got '{self.product_category.inner_text()}'"
        assert self.product_price.inner_text() == expected_details["price"], f"Expected price '{expected_details['price']}' but got '{self.product_price.inner_text()}'"
        assert self.product_availability.inner_text().endswith(expected_details["availability"]), f"Expected availability to end with '{expected_details['availability']}' but got '{self.product_availability.inner_text()}'"
        assert self.product_condition.inner_text().endswith(expected_details["condition"]), f"Expected condition to end with '{expected_details['condition']}' but got '{self.product_condition.inner_text()}'"
        assert self.product_brand.inner_text().endswith(expected_details["brand"]), f"Expected brand to end with '{expected_details['brand']}' but got '{self.product_brand.inner_text()}'" 

    def close_google_vignette(self):
        try:
            self.page.locator("text=Open").wait_for(timeout=3000)
            self.page.locator("text=Open").click()
        except:
            print("Ad not present, continuing test")