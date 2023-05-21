import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class oop_selium_1():
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", False) #false - это закрытие браузера после выполнения теста
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

oop_selium = oop_selium_1()
oop_selium.test_select_product()