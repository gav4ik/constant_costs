import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from selenium.webdriver.common.keys import Keys

class Test (unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://glosta.vps2078.mtu.immo/detail/")
        date_from = driver.find_element_by_id("date-from")
        date_from.send_keys("10.12.2019")
        date_to = driver.find_element_by_id("date-to")
        date_to.send_keys("11.12.2019")
        service = driver.find_element_by_id("service")
        drp = Select(service)
        drp.select_by_visible_text("Survey")
        # //*[@id="service"]/option[92]
        add_button = driver.find_element_by_id("add-service-button").click()
        # add_button.click()
        driver.implicitly_wait(5)
        galka = driver.find_element_by_class_name("select-all").click()
        #galka = driver.find_element_by_link_text('Выбрать все')
        # galka.click()
        driver.implicitly_wait(5)
        abon = driver.find_element_by_id("additional-param-name")
        abon.send_keys("msisdn")
        choose_button = driver.find_element_by_id("add-param-button")
        choose_button.click()
        driver.implicitly_wait(5)
        #tel = driver.find_element_by_class_name("additional-param form-control")
        tel = driver.find_element_by_xpath("//*[@id='additional-params']/li/input")
        tel.send_keys("79645860800")
        driver.implicitly_wait(5)
        show = driver.find_element_by_id("show-button")
        show.click()
        driver.implicitly_wait(5)
        # print(driver.page_source)
        # print(driver.title)
        # data = driver.find_element_by_xpath(//*[@id='data']/tbody/tr[2]/td[1]).
        # assert "2019-12-10" in driver.page_source
        # assert "2019-12-11" in driver.page_source
        # assert "Survey" in driver.page_source
        assert "*79645860800*" in driver.page_source
        #
        # self.assertEqual("")
        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/work/python/test1/reports'))
#         driver.close()
#
#
#         driver.quit()
#
#
# print("Test completed")