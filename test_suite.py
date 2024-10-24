import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from Login_Page.Login_Page_Test import Login_Page_Test


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = Login_Page_Test(driver)
    login_page.login_url("http://staging.legalconnectonline.com/legalconnect-portal-client/")
    return login_page


def test_login_page(login):
    login.email_field("graceuko@gmail.com")
    login.password_field("grace")
    login.click_login()
