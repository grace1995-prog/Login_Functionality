from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_Locator:
    Enter_Email = (By.XPATH, " //input[@id='Email']")
    Enter_Password =(By.XPATH," //input[@id='Password']")
    Login_Button=(By.XPATH,"//button[@id='login_button']")
