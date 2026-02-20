from playwright.sync_api import Playwright,expect

class ContactUsPage:
    def __init__(self,page:Playwright):
        self.page=page
        self.contact_us_link=self.page.get_by_role(role="link",name=" Contact us")
        self.contact_us_header=self.page.locator("h2", has_text='Get In Touch')
        self.name_input=self.page.locator("input[name='name']")
        self.email_input=self.page.locator("input[name='email']")   
        self.subject_input=self.page.get_by_placeholder("Subject")
        self.message_textarea=self.page.locator("textarea[name='message']")
        self.upload_file_input=self.page.locator("input[type='file']")
        self.submit_button=self.page.get_by_role(role="button",name="Submit")
        self.success_message=self.page.get_by_text("Success! Your details have been submitted successfully.")

    def click_contact_us(self):
        self.contact_us_link.click()    

    def verify_contact_us_header(self):
        assert self.contact_us_header.is_visible(),"Contact Us header is not visible"

    def fill_contact_form(self,name,email,subject,message,file_path):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_textarea.fill(message)
        self.upload_file_input.set_input_files(file_path)
        self.submit_button.click()
        self.page.on("dialog",lambda dialog: dialog.accept())

    def verify_success_message(self):
        print(self.success_message.inner_text())
        expect(self.success_message).to_be_visible()  # Using Playwright's expect for better error messages
        #assert self.success_message.is_visible(),"Success message is not visible after submitting contact form"

    


