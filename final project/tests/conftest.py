import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from utils import config

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Fixture that logs in before returning the driver"""
    driver.get(config.BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(config.USER_EMAIL, config.PASSWORD)
    return driver