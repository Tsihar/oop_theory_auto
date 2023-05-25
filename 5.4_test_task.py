import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password = 'secret_sauce'
for user_name in login:
    if user_name == 'standard_user':
        user_name_standard = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name_standard.send_keys(user_name)

        password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)

        page_products = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        page_title_text = page_products.text
        assert page_title_text == "Products"
        print("standard_user has opened 'Products' page")

        burger_menu_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        burger_menu_button.click()

        logout_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout_button.click()

        login_page = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='login_logo']")))
        login_page_title = login_page.text
        assert login_page_title == "Swag Labs"
        print("standard_user has logged out")

    elif user_name == 'locked_out_user':
        user_name_locked = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name_locked.send_keys(user_name)

        password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_field.send_keys(password)

        password_field.send_keys(Keys.RETURN)

        cross_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='error-button']")))
        cross_button.click()

        user_name_locked.clear()
        password_field.clear()
        time.sleep(2)

    elif user_name == 'problem_user':
        user_name_problem = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name_problem.send_keys(user_name)

        password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password_field.send_keys(password)
        print(password)

        password_field.send_keys(Keys.RETURN)

        page_products = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        page_title_text = page_products.text
        assert page_title_text == "Products"
        print("problem_user has opened 'Products' page")

        burger_menu_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        burger_menu_button.click()

        logout_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout_button.click()

        login_page = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='login_logo']")))
        login_page_title = login_page.text
        assert login_page_title == "Swag Labs"
        print("problem_user has logged out")


        # login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        # time.sleep(2)
        # login_button.click()









