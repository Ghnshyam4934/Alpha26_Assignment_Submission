from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurePage:
    """
    Page Object Model (POM) class for the Secure Area Page.

    This page appears after successful login.
    It contains elements and actions related to:
    - Secure Area heading validation
    - Logout operation
    - Flash message validation
    """

    # -------------------------------
    # Element Locators
    # -------------------------------

    # Secure Area heading locator (h2 tag contains "Secure Area")
    SECURE_HEADING = (By.TAG_NAME, "h2")

    # Logout button locator (CSS selector for logout button)
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")

    # Flash message locator (used to validate logout success message)
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        """
        Constructor:
        - Accepts driver instance passed from test script
        - Initializes explicit wait for stable execution
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_heading_text(self):
        """
        Fetch the Secure Area heading text.

        Purpose:
        - Used in test case assertion to confirm user is redirected
          to secure page after successful login.
        """
        return self.wait.until(EC.visibility_of_element_located(self.SECURE_HEADING)).text

    def click_logout(self):
        """
        Click on Logout button.

        Purpose:
        - Logs out the user from secure session.
        - Explicit wait ensures element is clickable before click action.
        """
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()

    def get_flash_message(self):
        """
        Fetch logout success message.

        Purpose:
        - Used to verify successful logout operation.
        """
        return self.wait.until(EC.visibility_of_element_located(self.FLASH_MESSAGE)).text
