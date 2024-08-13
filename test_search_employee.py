from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_pim_module(self):
        # Wait until the PIM module link is clickable and then click it
        pim_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'PIM')))
        pim_link.click()

    def click_add_employee(self):
        # Wait until the Add button is clickable and then click it
        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'btnAdd')))
        add_button.click()

    def fill_employee_details(self, first_name, last_name, other_details=None):
        # Wait until the first name field is visible and then fill in details
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'firstName')))
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, 'lastName')
        last_name_field.send_keys(last_name)

        if other_details:
            # Example for filling in other details if applicable
            # other_field = self.driver.find_element(By.ID, 'someOtherField')
            # other_field.send_keys(other_details)
            pass

    def click_save(self):
        # Wait until the Save button is clickable and then click it
        save_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'btnSave')))
        save_button.click()

    def get_success_message(self):
        # Wait until the success message is visible and retrieve it
        success_message_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.message.success')))
        return success_message_element.text


def test_add_new_employee():
    # Initialize WebDriver (Edge in this case)
    driver = webdriver.Edge()

    try:
        # Launch the Orange HRM site
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        # Log in with valid ESS-User account
        driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
        driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        driver.find_element(By.ID, 'btnLogin').click()

        # Create PIMPage instance and execute test steps
        pim_page = PIMPage(driver)

        # Step 1: Go to PIM module
        pim_page.go_to_pim_module()

        # Step 2: Click on Add and fill in employee details
        pim_page.click_add_employee()
        pim_page.fill_employee_details('John', 'Doe', 'Additional details if any')

        # Step 3: Save employee details
        pim_page.click_save()

        # Verify the expected result
        success_message = pim_page.get_success_message()
        assert 'Successfully Added' in success_message, f"Expected success message but got: {success_message}"

        print("Test case TC_PIM_01 passed successfully.")

    except Exception as e:
        print(f"Test case TC_PIM_01 failed: {e}")

    finally:
        # Close the browser
        driver.quit()


