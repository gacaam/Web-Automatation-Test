import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from page import HomePage

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Set up the ChromeDriver service
        PATH = "C:/Program Files (x86)/chromedriver.exe"
        service = Service(PATH)
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.demoblaze.com/index.html")
  
    def test_login(self):
        username = "username"
        login_page = HomePage(self.driver)
        login_page.login(username, "password")
        time.sleep(3)

        welcome_element = login_page.find_element(By.ID, "nameofuser")

        # assert true if "Welcome [username] appears in navbar"
        self.assertTrue(username in welcome_element.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


