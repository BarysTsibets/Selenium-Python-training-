from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
import time


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\driver\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("Automation Step by Step")
        time.sleep(2)
        self.driver.find_element_by_name("btnK").click()

    def test_search_la(self):
        self.driver.get("https://google.com")
        elem2 = self.driver.find_element_by_name("q")
        elem2.clear()
        elem2.send_keys("Los Angeles")
        self.driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=r'C:\Users\BorisPC\PycharmProjects\untitled\HelloWorld\Automation\reports'))
