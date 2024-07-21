import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page import HomePage, ProductPage


class TestPerformance(unittest.TestCase):
    def setUp(self):
        # Set up the ChromeDriver service
        PATH = "C:/Program Files (x86)/chromedriver.exe"
        service = Service(PATH)
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.demoblaze.com/index.html")
  
    def test_add_cart_performance(self):
        home_page = HomePage(self.driver)
        home_page.login("username", "password")
        time.sleep(3)

        home_page.open_product_page("Samsung galaxy s6")  
        
        product_page = ProductPage(self.driver)

        # measure the time it takes to add to cart
        start_time = time.time()
        product_page.add_to_cart() 

        # wait for the alert to be present
        product_page.wait_until_alert(10)

        end_time = time.time()
        add_to_cart_time = end_time - start_time

        print(f"Add to cart time: {add_to_cart_time} seconds")  

        # assert true if add to cart time is less than equal to 2
        self.assertLessEqual(add_to_cart_time, 2)  

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


