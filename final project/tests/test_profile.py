import pytest
from pages.profile_page import ProfilePage
from pages.go_to_profile_page  import GoToProfilePage

def test_verify_profile(logged_in_driver):
    driver = logged_in_driver
    go_profile=GoToProfilePage(driver)
    go_profile.go_to_profile()
    page=ProfilePage(driver)
    expected_first="Abhijit"
    expected_last="Kasbe"
    actual_first, actual_last = page.get_profile_name()

    assert actual_first == expected_first, f"First name mismatch! Expected: {expected_first}, Got: {actual_first}"
    assert actual_last == expected_last, f"Last name mismatch! Expected: {expected_last}, Got: {actual_last}"