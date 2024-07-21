from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"Element not found: {value}, Exception: {e}")
            return None
        
    def find_elements(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"Element not found: {value}, Exception: {e}")
            return None
        
    def wait_until_clickable(self, by, value, timeout):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

class HomePage(BasePage):
    def open_login_popup(self):
        login_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'login2'))
        )
        login_popup.click()

    def login(self, username: str, password: str):
        self.open_login_popup()
        username_field = self.find_element(By.ID, "loginusername")
        password_field = self.find_element(By.ID, "loginpassword")
        login_button = self.find_element(By.XPATH, '//button[text()="Log in"]')
       
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def open_product_page(self, product_name):
        product_link = self.find_element(By.XPATH, f"//a[text()='{product_name}']")
        product_link.click()

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.find_element(By.LINK_TEXT, "Add to cart")
        add_to_cart_button.click()

    def wait_until_alert(self, timeout):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

class CartPage(BasePage):
    def open_cart(self):
        cart_page = self.find_element(By.ID, 'cartur')
        cart_page.click()
        
    def is_item_in_cart(self, product_name):
        item_in_cart = self.find_element(By.XPATH, f"//td[contains(text(), '{product_name}')]")
        return item_in_cart is not None