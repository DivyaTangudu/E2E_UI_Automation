from playwright.sync_api import Playwright

class LoginPage:
    def __init__(self,page:Playwright):
        self.page=page
        self.login_link=self.page.get_by_role(role='link',name=" Signup / Login")
        self.login_header=self.page.locator("h2", has_text="Login to your account")
        self.email_input=self.page.locator(".login-form").get_by_role("textbox", name="Email Address")
        self.password_input=self.page.locator(".login-form").get_by_role("textbox", name="Password")
        self.login_button=self.page.locator(".login-form").get_by_role(role="button",name="Login")
        self.logout=self.page.get_by_role(role="link",name=" Logout")

    def click_login_link(self):
        self.login_link.click() 

    def verify_login_header(self):
        assert self.login_header.is_visible(),"Login header is not visible" 

    def fill_login_form(self,email,password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()   

    def userlogintext(self):
        return self.page.locator("a", has_text="Logged in as")
    
    def verify_error_message(self):
        error_message=self.page.get_by_text("Your email or password is incorrect!")
        assert error_message.is_visible(),"Error message for incorrect login is not visible"

    def verify_user_logout(self):
        self.logout.click()
        assert self.login_link.is_visible(),"Login link is not visible after logout"