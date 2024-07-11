
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class OrangeHRM:
    #this is OrangeHRM login website
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.login()
    
    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        username_box = driver.find_element(By.XPATH,'//input[@name="username"]')
        username_box.clear()
        username_box.send_keys(self.username)
        time.sleep(2)

        password_box = driver.find_element(By.XPATH,'//input[@name="password"]')
        password_box.clear()
        password_box.send_keys(self.password)
        time.sleep(2)

        login_box = driver.find_element(By.XPATH,'//button[@type="submit"]')
        login_box.click()
        time.sleep(3)

        logout_box = driver.find_element(By.XPATH,'//li[@class="oxd-userdropdown"]')
        time.sleep(2)
        logout_box.click()

        logout = driver.find_element(By.XPATH,'//a[@href="/web/index.php/auth/logout"]')
        time.sleep(2)
        logout.click()

username = "Admin"
password = "admin123"
OM = OrangeHRM(username,password)
input("Press Enter to close...")


