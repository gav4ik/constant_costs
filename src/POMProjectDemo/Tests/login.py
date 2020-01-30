import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from src.POMProjectDemo.Pages.loginPage import LoginPage
from src.POMProjectDemo.Pages.HomePage import HomePage



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/naryshkina/AppData/Local/Microsoft/WindowsApps/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver  # чтобы не писать self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)  # создаем класс
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(10)

    def test_02_login_invalid_username(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)  # создаем класс
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element_by_id("").text
        self.assertEqual(message, "Invalid credentials")

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/work/python/test1/src/TestsReports'))
