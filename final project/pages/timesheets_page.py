from seleniumpagefactory import PageFactory
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TimesheetsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        
    locators = {
        "select_project": ('CSS', '#active_projects'),
        "date": ('CSS', '#date-0'),
        "select_duration": ('CSS', '#duration-0'),
        "description": ('CSS', '#user_time_sheets_attributes_0_description'),
        "save_btn": ("XPATH", "//input[@type='submit' and @value='Save']"),
        "flash_msg": ("ID", "flashes")   
    }
    def fill_timesheet(self, project_name, date, duration, description):
        print("DEBUG: Selecting project:", project_name)
        self.select_project.select_element_by_text(project_name)
        print("DEBUG: Setting date:", date) 
        #self.date.set_text(date)
        self.driver.execute_script("arguments[0].value = arguments[1];", self.date, date)
        print("DEBUG: Selecting duration:", duration)
        self.select_duration.select_element_by_text(duration)
        print("DEBUG: Entering description:", description)
        self.description.set_text(description)
        print("DEBUG: Clicking save button")
        self.save_btn.click()

    def verify_date_format(self):
        date_value = self.date.get_attribute("value")
        print("DEBUG: Date field value is:", date_value)
        assert re.match(r"\d{4}-\d{2}-\d{2}", date_value), f"Invalid date format: {date_value}"
    def get_flash_message(self, timeout=10):
        flash_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.ID, "flashes"))
        )
        return flash_element.text.strip()