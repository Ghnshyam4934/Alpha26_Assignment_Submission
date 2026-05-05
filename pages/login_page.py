from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object Model (POM) class for the Login Page.

    This class contains:
    - Page URL
    - Locators for login elements
    - Reusable methods to perform actions on login page

    Benefits of POM:
    - Keeps locators and page actions in one place
    - Test scripts become clean and readable
    - Easy maintenance (if UI changes, update only here)
    """

    # URL of login page
    URL = "https://the-internet.herokuapp.com/login"

    # -------------------------------
    # Element Locators
    # -------------------------------
    # By.ID is used because ID is stable and faster than XPath
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")

    # CSS Selector used for login button
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Flash message is used for both success and error message validation
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        """
        Constructor:
        - Accepts driver instance from PyTest fixture
        - Initializes WebDriverWait for explicit waits
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """
        Opens the login page URL.
        This is the starting point of login automation.
        """
        self.driver.get(self.URL)

    def enter_username(self, username):
        """
        Enters username into username input field.
        Steps:
        - Wait until element is visible
        - Clear existing value
        - Enter new username
        """
        element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        """
        Enters password into password input field.
        Steps:
        - Wait until element is visible
        - Clear existing value
        - Enter password
        """
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    def click_login(self):
        """
        Clicks on Login button.
        Uses explicit wait to ensure button is clickable.
        """
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username, password):
        """
        Reusable method to perform complete login action.
        This reduces repeated code in test scripts.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        """
        Fetches the success/error message shown after login attempt.
        Used for assertions in test cases.
        """
        return self.wait.until(EC.visibility_of_element_located(self.FLASH_MESSAGE)).text
