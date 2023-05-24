from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Login_page import Login_page


# УРОК 5.1
# после каждого шага проверяем код комментя его, но оставляя раскоменченым экз класса и обращение к ф-ции
class Test_1():
    # шаг 1
    def test_select_product(self): # метод с помощью которого, мы выбираем опред товар на странице товаров
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True) #false - это закрытие браузера после выполнения теста
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        # для кода выше проверить что открывается окно браузера
        # шаг 2
# УРОК 5.2 (в уроке 5.3 мы удаляем ввод логина, т к указываем их там)
#         print("Start test") # отсюда мы далее начинаем наш тест
#         # шаг 3 ниже вставляем код с логином и паролем и авторизацией на сайте
        login_standard_user = "standard_user"
        password_all = "secret_sauce"
#
#         # далее будем испольЗОВАТЬ поиск локаторов вместе с явным ожиданием, так как это правильная практика
#         # поэтому все локаторы заменим на локаторы с явным ожиданием(+ импорт библиотек)
#         user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
#         user_name.send_keys(login_standard_user)
#         print("input login")
#
#         password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
#         password.send_keys(password_all)
#         print("input password")
#
#         password.send_keys(Keys.RETURN)
# Урок 5.3 заменяем ввод логина и пароля что выше на экземпляр класса Login_page
        login = Login_page(driver) # по факту класс login_page подтягивает наш драйвер из класса Test_1
        login.authorization(login_standard_user, password_all) # обращаемся к методу авторизации для авторизации
        # система подсказывает, что нужны 2 обяз атрибута логин и пароль

        """Выбор товара"""
        # ищем локатор кнопки add to cart для первого товара
        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("1st item added to the cart")

        """Клик по корзине"""
        open_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        open_cart.click()
        print("transfer to cart")

        """Верификация нахождения на странице корзины"""
        # проверка того, что мы перешли в корзину по названию страницы (не используем в данном тесте название товара в корзине и цену, просто названия страницы достаточно)
        success = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        success_value = success.text
        assert success_value == 'Your Cart'
        print("cart is opened")

test = Test_1()
test.test_select_product()
