from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from django.test import LiveServerTestCase
from django.urls import reverse
import os

class LoginTest(LiveServerTestCase):

    def setUp(self):
        service = Service(os.path.join(os.getcwd(), 'chromedriver.exe'))
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10) 

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        self.driver.get(self.live_server_url + reverse('login'))
        self.driver.find_element(By.NAME, 'username').send_keys('student')
        self.driver.find_element(By.NAME, 'password').send_keys('Password123')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        
        # Check if redirected to success page
        self.assertEqual(self.driver.current_url, self.live_server_url + reverse('success'))

    def test_login_invalid_username(self):
        self.driver.get(self.live_server_url + reverse('login'))
        self.driver.find_element(By.NAME, 'username').send_keys('wronguser')
        self.driver.find_element(By.NAME, 'password').send_keys('Password123')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        
        # Verify error message
        error_message = self.driver.find_element(By.CLASS_NAME, 'error').text
        self.assertIn("Your username is invalid!", error_message)

    def test_login_invalid_password(self):
        self.driver.get(self.live_server_url + reverse('login'))
        self.driver.find_element(By.NAME, 'username').send_keys('student')
        self.driver.find_element(By.NAME, 'password').send_keys('wrongpassword')
        self.driver.find_element(By.TAG_NAME, 'button').click()
        
        # Verify error message
        error_message = self.driver.find_element(By.CLASS_NAME, 'error').text
        self.assertIn("Your password is invalid!", error_message)