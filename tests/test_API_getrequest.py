import json
from playwright.sync_api import Page,expect

def test_get_request(page:Page):
    request=page.request.get("https://automationexercise.com/api/productsList")
    assert request.status==200,"API request failed"
    response_data=request.json()
    response=json.dumps(response_data, indent=2)
    #print(response)
    brand_names={products["brand"] for products in response_data["products"]}
    print(brand_names)