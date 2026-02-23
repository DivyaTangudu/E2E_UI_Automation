from playwright.sync_api import Playwright,expect

class SearchPage():
    def __init__(self,page:Playwright):
        self.page=page
        self.products_link=self.page.get_by_role(role="link",name="Products")
        self.allproducts_header=self.page.locator("h2", has_text="All Products")
        self.serchbutton=self.page.locator("#search_product")
        self.submitsearch=self.page.locator("#submit_search")
        self.search_results=self.page.locator(".features_items").locator(".col-sm-4")

    def navigate_to_products_page(self):
        self.products_link.click()

    def verify_all_products_header(self):
        assert self.allproducts_header.is_visible(),"All products header is not visible"

    def search_product(self,product_name):
        self.serchbutton.fill(product_name)
        self.submitsearch.click()

    def verify_search_results(self,expected_product_name):
        count=self.search_results.count()
        assert count > 0, "No search results found"
        for i in range(count):
            product_title=self.search_results.nth(i).locator(".productinfo p").inner_text()
            print(f"Search result {i+1}: {product_title}")
            assert expected_product_name in product_title, f"Expected product name '{expected_product_name}' not found in search result '{product_title}'"