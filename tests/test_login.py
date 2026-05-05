from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_valid_login_logout(driver):
    """
    Test Case: Validate successful login and logout flow.
    Steps:
    1. Open login page
    2. Login with valid credentials
    3. Verify Secure Area is displayed
    4. Logout and verify redirection back to login page
    """
    login_page = LoginPage(driver)
    secure_page = SecurePage(driver)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    heading = secure_page.get_heading_text()
    assert "Secure Area" in heading

    secure_page.click_logout()

    # Validate user redirected to login page
    assert "/login" in driver.current_url

    # Validate logout success message
    message = login_page.get_flash_message()
    assert "You logged out of the secure area!" in message


def test_invalid_login(driver):
    """
    Test Case: Validate failed login scenario.
    Steps:
    1. Open login page
    2. Login with invalid credentials
    3. Verify error message is displayed
    """
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("wronguser", "wrongpass")

    # Validate user remains on login page
    assert "/login" in driver.current_url

    # Validate correct error message displayed
    message = login_page.get_flash_message()
    assert "Your username is invalid!" in message or "Your password is invalid!" in message
