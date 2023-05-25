import time

from selenium import webdriver
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

login = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
password = "secret_sauce"

"""Create class instance 'page_products'. Class 'Products_page' contains 'login_verification' and 'logout' methods"""
page_products = Products_page(driver)

"""Login/logout by standard_user"""
for user_name in login[:1]:
    user_name_standard = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name_standard.send_keys(user_name)
    print(user_name)

    password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    page_products.login_verification()
    print("standard_user has opened 'Products' page")

    page_products.logout()
    print("standard_user has logged out")
    time.sleep(2)

"""Login by locked_out_user"""
for user_name in login[1:2]:
    user_name_locked = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name_locked.send_keys(user_name)
    print(user_name)

    password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    cross_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='error-button']")))
    cross_button.click()

    user_name_locked.clear()
    password_field.clear()
    time.sleep(2)

"""Login by problem_user"""
for user_name in login[2:3]:
    user_name_problem = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name_problem.send_keys(user_name)
    print(user_name)

    password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password_field.clear()  # этот clear фиксит мне проблему двойного ввода пароля в след шаге, я много чего пробовал, времени кучу потратил, но только этот clear мне помог
    # может я чего упустил, как-то не до конца как будто понимаю цикл for, но решение только такое нашел.
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    page_products.login_verification()
    print("problem_user has opened 'Products' page")

    page_products.logout()
    print("problem_user has logged out")

"""Login by performance_glitch_user"""
for user_name in login[3:]:
    user_name_glitch = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
    user_name_glitch.send_keys(user_name)
    print(user_name)

    password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    page_products.login_verification()
    print("performance_glitch_user has opened 'Products' page")

    page_products.logout()
    print("performance_glitch_user has logged out")
