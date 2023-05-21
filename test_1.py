from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# УРОК 5.1
# после каждого шага проверяем код комментя его, но оставляя раскоменченым экз класса и обращение к ф-ции
class Test_1():
    # шаг 1
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True) #false - это закрытие браузера после выполнения теста
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        # для кода выше проверить что открывается окно браузера
        # шаг 2
# УРОК 5.2
        print("Start test") # отсюда мы далее начинаем наш тест
        # шаг 3 ниже вставляем код с логином и паролем и авторизацией на сайте
        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        # далее будем испольЗОВАТЬ поиск локаторов вместе с явным ожиданием, так как это правильная практика
        # поэтому все локаторы заменим на локаторы с явным ожиданием(+ импорт библиотек)
        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_standard_user)
        print("input login")

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(password_all)
        print("input password")

        password.send_keys(Keys.RETURN)

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

        #ниже практика гита
        """Insert personal user information"""
        first_name = driver.find_element(by=By.XPATH, value="//input[@id='first-name']")
        first_name.send_keys("Igor")
        print("First name is entered")

        last_name = driver.find_element(by=By.XPATH, value="//input[@id='last-name']")
        last_name.send_keys("T")
        print("Last name is entered")

        postal_code = driver.find_element(by=By.XPATH, value="//input[@id='postal-code']")
        postal_code.send_keys("123456")


test = Test_1()
test.test_select_product()
