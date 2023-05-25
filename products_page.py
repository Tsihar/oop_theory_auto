from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Products_page():
    def __init__(self, driver):
        self.driver = driver

    def login_verification(self):
        page_products = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        page_title_text = page_products.text
        assert page_title_text == "Products"

    def logout(self):
        burger_menu_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        burger_menu_button.click()

        logout_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout_button.click()

        login_page = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='login_logo']")))
        login_page_title = login_page.text
        assert login_page_title == "Swag Labs"