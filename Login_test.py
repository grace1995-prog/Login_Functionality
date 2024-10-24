from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

driver.get("http://staging.legalconnectonline.com/legalconnect-portal-client/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#Email").send_keys("gracybaby1995@gmail.com")
time.sleep(15)
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("Imokom34@")
time.sleep(10)
driver.find_element(By.XPATH, "//button[@id='login_button']").click()
driver.quit()



