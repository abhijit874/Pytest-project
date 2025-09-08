from seleniumpagefactory import PageFactory

class ProfilePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    locators={
        "first_name":('CSS','#public_profile_first_name'),
        "last_name":('CSS','#public_profile_last_name')
    }
    def get_profile_name(self):
        actual_first = self.first_name.get_attribute("value")
        actual_last = self.last_name.get_attribute("value")
        return actual_first, actual_last