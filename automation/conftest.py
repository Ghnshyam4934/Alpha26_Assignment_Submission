import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    PyTest Fixture: driver()

    Purpose:
    - This fixture is responsible for setting up the Selenium WebDriver instance
      before each test case runs.
    - It also ensures that the browser is properly closed after test execution.

    Why we use fixture:
    - Avoid repeating browser setup code in every test file.
    - Keeps automation framework clean and maintainable.
    - Automatically manages setup and teardown in PyTest.

    Fixture Scope:
    - Default scope is 'function', meaning a new browser instance will open
      for every test case. This ensures clean execution and avoids session issues.
    """

    # Create Chrome browser configuration options
    options = webdriver.ChromeOptions()

    # This opens Chrome in maximized mode (better for UI visibility and element detection)
    options.add_argument("--start-maximized")

    # Setup ChromeDriver automatically using webdriver-manager.
    # webdriver-manager downloads the correct ChromeDriver version based on installed Chrome.
    # This avoids manual driver download and version mismatch errors.
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Implicit Wait:
    # Selenium will wait up to 3 seconds while searching for elements before throwing an exception.
    # This is a small safety buffer for minor page load delays.
    driver.implicitly_wait(3)

    # Yield returns the WebDriver instance to the test case.
    # Code after yield will execute once test case finishes (teardown part).
    yield driver

    # Teardown:
    # Quit closes all browser windows and ends WebDriver session properly.
    # Prevents memory leak and zombie Chrome processes.
    driver.quit()
