from playwright.sync_api import Playwright,expect

class PlaceorderPage:
    def __init__(self,page:Playwright):
        self.page=page
        self.product=self.page.locator(".fa fa-shopping-cart")
        self.addtocartbtn=self.product.locator("a",has_text="Add to cart")
        self.continuesshoppingbtn=self.page.locator(".btn btn-success close-modal btn-block")
        self.viewcartbtn=self.page.get_by_role(role="link",name="View Cart")    
        self.proceedtocheckoutbtn=self.page.get_by_role(role="link",name="Proceed To Checkout")
        self.placeorderbtn=self.page.get_by_role(role="button",name="Place Order")
        self.nameoncard=self.page.locator("input[name='name_on_card']")
        self.cardnumber=self.page.locator("input[name='card_number']")
        self.cvc=self.page.locator("input[name='cvc']")
        self.expiry_month=self.page.locator("input[name='expiry_month']")
        self.expiry_year=self.page.locator("input[name='expiry_year']")
        
    def add_product_to_cart(self):
        self.addtocartbtn.click()
        self.continuesshoppingbtn.click()

    def view_cart(self):
        self.viewcartbtn.click()

    def proceed_to_checkout(self):
        self.proceedtocheckoutbtn.click()

    def fill_payment_details(self,name_on_card,card_number,cvc,expiry_month,expiry_year):
        self.nameoncard.fill(name_on_card)
        self.cardnumber.fill(card_number)
        self.cvc.fill(cvc)
        self.expiry_month.fill(expiry_month)
        self.expiry_year.fill(expiry_year) 

    def place_order(self):
        self.placeorderbtn.click()

