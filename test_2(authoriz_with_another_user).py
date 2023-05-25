from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Login_page import Login_page
# урок 5.3 логинимся под проблемным юзером problem_user - тест: логин проблемныйм юзером
# в итоге чтоб создать второй тест надо было всего-то скопипастить тест, поменять назв класса, логин, и экз класса
class Test_2():
    def test_select_product(self): # метод с помощью которого, мы выбираем опред товар на странице товаров
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True) #false - это закрытие браузера после выполнения теста
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        login_problem_user = "problem_user"
        password_all = "secret_sauce"

        login = Login_page(driver)
        login.authorization(login_problem_user, password_all)

        """Выбор товара"""

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("1st item added to the cart")

        """Клик по корзине"""
        open_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        open_cart.click()
        print("transfer to cart")

        """Верификация нахождения на странице корзины"""
        success = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        success_value = success.text
        assert success_value == 'Your Cart'
        print("cart is opened")

test = Test_2()
test.test_select_product()
