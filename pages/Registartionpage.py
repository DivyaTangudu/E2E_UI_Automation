import random
from playwright.sync_api import Page,expect

class RegistrationPage:
    def __init__(self,page:Page):
        self.page=page
        #homepage
        self.signup=self.page.get_by_role(role='link',name=" Signup / Login")
        #signup page validation
        self.siguptext=self.page.locator("h2", has_text="New User Signup!")
        #signup form
        self.name=self.page.get_by_placeholder("Name")
        self.email=self.page.locator(".signup-form").get_by_role("textbox", name="Email Address")
        self.sighupbtn=self.page.locator(".signup-form").get_by_role(role="button",name="Signup")
        #create account page
        self.signup_text=self.page.get_by_text("Enter Account Information")
        self.gender=self.page.locator("#id_gender2")
        self.password=self.page.locator("#password")
        self.days=self.page.locator("#days")
        self.month=self.page.locator("#months")
        self.year=self.page.locator("#years")
        self.news_letter=self.page.get_by_role(role="checkbox",name="newsletter")
        self.optin=self.page.locator("#optin")
        self.first_name=self.page.locator("#first_name")
        self.lastname=self.page.locator("#last_name")
        self.comapny=self.page.locator("#company")
        self.address=self.page.locator("#address1")
        self.country=self.page.locator("#country")
        self.state=self.page.locator("#state")
        self.city=self.page.locator("#city")
        self.zipcode=self.page.locator("#zipcode")
        self.mobileno=self.page.locator("#mobile_number")
        self.create_acnt_btn=self.page.get_by_role(role="button",name="Create Account")

        #Post account creation
        self.account_created=self.page.get_by_text("Account Created!")
        self.continuebutton=self.page.get_by_role(role="link",name="Continue")
        self.userlogintext=lambda: self.page.locator("a", has_text="Logged in as")
       
        #account deletion
        self.deleteaccout=self.page.get_by_role(role="link",name=" Delete Account")
        self.deletetext=self.page.get_by_text("Account Deleted!")
        
    def clicksignup(self):
        self.signup.click()
        
    def verify_signup_header(self):
        assert self.siguptext.is_visible(),"New User Sign In header is not visible"

    def fill_signup_form(self,username,email):
        self.name.fill(username)
        self.email.fill(email)
        self.sighupbtn.click()  

    def verify_account_info_text(self):
        assert self.signup_text.is_visible(),"not asking for account info yet"  

    def fill_account_info(
        self,
        password,
        first_name,
        last_name,
        company,
        address,
        country,
        state,
        city,
        zipcode,
        mobile_number,
        dob
    ):
        self.gender.click()
        self.password.fill(password)

        # Parse DOB
        year, month, day = dob.split("-")
        self.days.select_option(day.lstrip("0"))
        self.month.select_option(str(int(month)))
        self.year.select_option(year)
        self.news_letter.click()
        self.optin.click()
        self.first_name.fill(first_name)
        self.lastname.fill(last_name)
        self.comapny.fill(company)
        self.address.fill(address)
        self.country.select_option(country)         
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(str(zipcode))          
        self.mobileno.fill(str(mobile_number))
        self.create_acnt_btn.click()    

    def verify_account_creation(self):
            assert self.account_created.is_visible(), "Accout creation failed"
        
    def verify_user_logged_in(self):
        # Wait for the user login text to appear, print page content if not found
            self.page.wait_for_selector("a:has-text('Logged in as')", timeout=5000)
            assert self.userlogintext().is_visible(), "User login text not visible"

    def continue_after_account_creation(self):
        self.continuebutton.click()
             
    def delete_account(self):
        self.deleteaccout.click()

    def verify_account_deletion(self):
        assert self.deletetext.is_visible(), "Account deletion failed"
            

    @staticmethod
    def generate_random_email():
        return f"user{random.randint(1000, 9999)}@gmail.com"