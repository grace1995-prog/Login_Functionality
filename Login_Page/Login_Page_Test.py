import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Login_Locator.Login_Locator_Test import Login_Locator


class Login_Page_Test:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def email_field(self,email_field):
        email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_Locator.Enter_Email))
        email_address.send_keys(email_field)
        time.sleep(5)

    def password_field(self,password_field):
        submit_password = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(Login_Locator.Enter_Password))
        submit_password.send_keys(password_field)
        time.sleep(2)

    def click_login(self):
        click_button = WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located(Login_Locator.Login_Button))
        click_button.click()
        time.sleep(2)

