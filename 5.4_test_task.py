import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from products_page import Products_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'

page_products = Products_page(driver)

for user_name in login:
    try:
        user_name_login = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name_login.send_keys(user_name)
        print(user_name)

        password_field = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_field.clear()
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)

        page_products.login_verification()
        print("standard_user has opened 'Products' page")

        page_products.logout()
        print("standard_user has logged out")

    except TimeoutException as exception:
        print("TimeoutException is received")
        cross_button = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='error-button']")))
        cross_button.click()
        user_name_login.clear()
        password_field.clear()











