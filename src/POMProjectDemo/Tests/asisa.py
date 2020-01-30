from selenium import webdriver
import unittest



class Test (unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://intranet.immo/sms-tests/index.php")

