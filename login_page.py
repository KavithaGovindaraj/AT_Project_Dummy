# login_page

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def open(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "oxd-button"))
        )
        login_button.click()

    def get_welcome_message(self):
        welcome_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
        )
        return welcome_message_element.text

