from seleniumpagefactory import PageFactory

class GoToProfilePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators={
        "profile":('LINK_TEXT','Profile')
    }
    
    def go_to_profile(self):   
        self.profile.click()
    