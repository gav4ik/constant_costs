import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:/Users/naryshkina/AppData/Local/Microsoft/WindowsApps/chromedriver.exe")
        driver.get("https://google.com/")
        driver.maximize_window()
        titleOfWebPage = driver.title
        #assertEqual
        self.assertEqual("Google123", titleOfWebPage, "Webpage title is not same")
        # self.assertNotEqual("Google123", titleOfWebPage)


if __name__=="main":
    unittest.main()