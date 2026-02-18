import pytest
import pandas as pd
from playwright.sync_api import Playwright,expect
from pages.Registartionpage import RegistrationPage

# Read Excel and convert to list of dicts
excel_file = "data/test_data.xlsx"
df = pd.read_excel(excel_file)
test_data = df.to_dict("records")

@pytest.mark.parametrize("user_data",test_data)
def test_registration(playwright:Playwright,browser_context,user_data):
    
    page = browser_context.new_page()
    page.goto("http://automationexercise.com")
    registration=RegistrationPage(page)
    registration.clicksignup()
    registration.verify_signup_header()
    username="testuser"
    email=RegistrationPage.generate_random_email()  
    registration.fill_signup_form(username,email)
    registration.verify_account_info_text()
    registration.fill_account_info(
        password=user_data["password"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        company=user_data["company"],
        address=user_data["address"],
        country=user_data["country"],
        state=user_data["state"],
        city=user_data["city"],
        zipcode=user_data["zipcode"],
        mobile_number=user_data["mobile_number"],
        dob=user_data["dob"]
    )
    registration.verify_account_creation()
    registration.continue_after_account_creation()
    registration.verify_user_logged_in()
    registration.delete_account()
    registration.verify_account_deletion()  