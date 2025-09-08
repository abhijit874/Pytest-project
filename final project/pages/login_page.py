from seleniumpagefactory.Pagefactory import PageFactory

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "user_email": ('CSS', '#user_email'),
        "password": ('CSS', '#user_password'),
        "loginBtn": ('CSS', 'body > div.d-flex.h-100 > section.form-wrapper.d-flex.flex-column.justify-content-center.align-items-center.w-50.h-100 > div.w-45.p-6.border.rounded.mx-auto > form > input.btn.btn-secondary'),
        "flash_message":('ID','flashes')
    }

    def login(self, user_email, password):
        self.user_email.set_text(user_email)
        self.password.set_text(password)
        self.loginBtn.click()

    def get_flash_message(self):
        return self.flash_message.get_text()