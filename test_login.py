import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope="module")
def driver():
    # Setup the Edge WebDriver
    driver = webdriver.Edge()
    # Implicitly wait for elements to appear
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_successful_login(driver):
    try:
        # Open the login page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Attempt to log in with valid credentials
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()

        # Explicitly wait for the welcome message to appear
        welcome_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
        ).text

        # Debug output to understand what message is actually returned
        print(f"Actual welcome message: {welcome_message}")

        # Assert that the welcome message is not empty
        assert welcome_message, "Welcome message should not be empty."

    except NoSuchElementException as e:
        pytest.fail(f"Test failed due to missing element: {e}")


def test_unsuccessful_login(driver):
    try:
        # Open the login page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Attempt to log in with invalid credentials
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("wrongPassword")
        driver.find_element(By.CLASS_NAME, "oxd-button").click()

        # Explicitly wait for the error message to appear
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))
        ).text

        # Assert that the error message is displayed
        assert "Invalid credentials" in error_message, f"Expected 'Invalid credentials', but got '{error_message}'"

    except NoSuchElementException as e:
        pytest.fail(f"Test failed due to missing element: {e}")


if __name__ == "__main__":
    pytest.main()