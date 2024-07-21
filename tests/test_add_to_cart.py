import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page import HomePage, ProductPage, CartPage

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        # Set up the ChromeDriver service
        PATH = "C:/Program Files (x86)/chromedriver.exe"
        service = Service(PATH)
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.demoblaze.com/index.html")
  
    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.login("username", "password")
        time.sleep(3)

        home_page.open_product_page("Samsung galaxy s6")  
        
        product_page = ProductPage(self.driver)
        product_page.add_to_cart() 

        cart_page = CartPage(self.driver)
        cart_page.open_cart()

        # assert true if item is in cart
        self.assertTrue(cart_page.is_item_in_cart("Samsung galaxy s6"), "Item not found in cart.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
