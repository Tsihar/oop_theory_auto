# в будущем у каждой нашей страницу будет отдельный класс, отд метод, кот будет содержать в себе свои локаторы, свои шаги и действия, кот будут совершаться на данной странице
# такие как авторизация, поэтому их надо выносить в отдельные модули, чтобы,
# если там что-то поменяется мы поменяли только один файл, а не в каждом тесте меняли, к прим xpath.
# Такие модули будут содержать свои классы и методы.
# Этот принцип наз-ся - Page object model.
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page():
    # далее прописываем обяз атрибуты данного класса
    def __init__(self, driver): # в данном методе мы будем хранить шаги отвечающие за авторизацию
        self.driver = driver

    def authorization(self, login_name, login_password): # 2 обяз атрибута логин и пароль
        # login_standard_user = "standard_user" # эти 2 переменные не понадообятся, т к будут вводится в файле test_1
        # password_all = "secret_sauce"

        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print("input login")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(login_password)
        print("input password")

        password.send_keys(Keys.RETURN)




