import unittest
from selenium import webdriver
from src.Page import Page
import time

class VerifyAsisaStata (unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/naryshkina/AppData/Local/Microsoft/WindowsApps/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_check_sms(self):
        driver = self.driver
        driver.get("http://intranet.immo/sms-tests/index.php")
        time.sleep(2)
