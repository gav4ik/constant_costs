import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
import HtmlTestRunner
from selenium import webdriver
from src.Page import Page
import time
import unittest


class VerifySearchStata (unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/naryshkina/AppData/Local/Microsoft/WindowsApps/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_stata_msisdn(self):
        driver = self.driver

        driver.get("http://glosta.vps2078.mtu.immo/detail/")

        stata = Page(driver)
        stata.enter_data_from("10.12.2019")
        stata.enter_data_to("11.12.2019")
        stata.choose_service("Survey")
        time.sleep(2)
        stata.click_select_all()
        time.sleep(2)
        stata.enter_additional_param("msisdn")
        time.sleep(2)
        stata.click_additional_param()
        time.sleep(2)
        stata.fulfil_param('79645860800')
        time.sleep(7)
        stata.show_click()
        time.sleep(2)

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/work/python/test1/src/TestsReports'))


