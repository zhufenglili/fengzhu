from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Testl:
    def setup(self):
        #复用浏览器 复用端口922 先设置opton
        option=Options()
        #设置debugger地址
        option.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option) #复用浏览器这里也要加option参数
        # self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown(self):
    # self.driver.quit()
    def test_1(self):
     self.driver.find_element_by_id("kw").send_keys('sdjfksdjf')
     self.driver.find_element_by_id("su").click()


