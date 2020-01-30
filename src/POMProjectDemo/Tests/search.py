import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time
import HtmlTestRunner



class VerifySearchTestScenario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/naryshkina/AppData/Local/Microsoft/WindowsApps/chromedriver.exe")

    def test_01_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        driver.maximize_window()
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN) # нажать enter (перевод каретки)
        time.sleep(5)
        assert "PyCon AU 2018" in driver.page_source
        print("Test completed")

    def test_02_search_failed_in_python_org(self):
         driver = self.driver
         driver.get("https://www.python.org/")
         driver.maximize_window()
         self.assertIn("Python", driver.title)
         elem = driver.find_element_by_id("id-search-field")
         elem.send_keys("pycon")
         elem.send_keys(Keys.RETURN)
         time.sleep(5)
         assert "PyCon AU 2020" in driver.page_source
         print("Can't find! Test failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/work/python/test1/src/TestsReports'))




