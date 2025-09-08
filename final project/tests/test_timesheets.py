import pytest
from pages.timesheets_page import TimesheetsPage
from pages.dashboard_page import DashboardPage
def test_add_timesheet(logged_in_driver):
    driver = logged_in_driver
    dashboard = DashboardPage(driver)
    dashboard.go_to_new_timesheet()
    page = TimesheetsPage(driver)
    
    page.fill_timesheet(
        project_name="Event - Event",
        date="2025-08-26",
        duration="8 hours",
        description="Worked on final project module"
    )

    page.verify_date_format()
    flash_text = page.get_flash_message()
    assert flash_text == "Timesheet created successfully"