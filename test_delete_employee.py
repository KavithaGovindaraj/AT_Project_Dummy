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
        # Navigate to the PIM module
        pim_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'PIM')))
        pim_link.click()

    def search_employee(self, employee_name):
        # Enter the employee name in the search box and submit the search
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'empsearch_employee_name_empName')))
        search_box.clear()
        search_box.send_keys(employee_name)
        search_button = self.driver.find_element(By.ID, 'searchBtn')
        search_button.click()

    def select_employee_to_delete(self):
        # Select the employee from the list (assuming a checkbox)
        checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, 'chkSelectRow[]')))
        checkbox.click()

    def click_delete_button(self):
        # Click the delete button to delete the selected employee
        delete_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'btnDelete')))
        delete_button.click()

    def confirm_deletion(self):
        # Confirm the deletion in the confirmation dialog
        confirm_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'dialogDeleteBtn')))
        confirm_button.click()

    def get_success_message(self):
        # Retrieve the success message after deletion
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.message.success'))).text


def test_delete_employee():
    # Initialize WebDriver (Edge in this case)
    driver = webdriver.Edge()

    try:
        # Launch the Orange HRM site
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        # Log in with a valid ESS-User account
        driver.find_element(By.ID, 'txtUsername').send_keys('valid_username')
        driver.find_element(By.ID, 'txtPassword').send_keys('valid_password')
        driver.find_element(By.ID, 'btnLogin').click()

        # Create PIMPage instance and execute test steps
        pim_page = PIMPage(driver)

        # Step 1: Go to PIM module
        pim_page.go_to_pim_module()

        # Step 2: Search for an existing employee
        pim_page.search_employee('John Doe')

        # Step 3: Select the employee to delete
        pim_page.select_employee_to_delete()

        # Step 4: Click the delete button and confirm deletion
        pim_page.click_delete_button()
        pim_page.confirm_deletion()

        # Verify the expected result
        success_message = pim_page.get_success_message()
        assert 'Successfully Deleted' in success_message, f"Expected success message but got: {success_message}"

        print("Test case TC_PIM_03 passed successfully.")

    except Exception as e:
        print(f"Test case TC_PIM_03 failed: {e}")

    finally:
        # Close the browser
        driver.quit()

