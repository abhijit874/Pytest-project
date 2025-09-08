from seleniumpagefactory import PageFactory

class DashboardPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "timesheets":('CSS','body > div.d-flex.h-100 > aside > nav > a:nth-child(4)'),
        "new_timesheet":('CSS','body > div.d-flex.h-100 > main > header > div > div > a')
    }

    def go_to_new_timesheet(self):
        self.timesheets.click()
        self.new_timesheet.click()