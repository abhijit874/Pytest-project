import pytest
from pages.login_page import LoginPage
from utils import config

def test_valid_login(driver):
    driver.get(config.BASE_URL )
    login_page = LoginPage(driver)
    login_page.login(config.USER_EMAIL, config.PASSWORD)
    flash_text = login_page.get_flash_message()
    assert flash_text.strip() == "Signed in successfully."