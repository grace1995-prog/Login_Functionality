from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()
driver.get("https://staging.legalconnectonline.com/legalconnect-website-angular/")
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element(By.XPATH, "/html/body/lc-root/app-site/div/mat-toolbar/div/div[2]/div[2]/a[1]").click()
time.sleep(10)
driver.find_element(By.XPATH, "//div[@id='cdk-overlay-0']").click()
time.sleep(20)
driver.find_element(By.XPATH, "//body/div[1]/div[2]/div[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//body/div[1]/div[2]/div[1]/div[1]").click()
driver.quit()