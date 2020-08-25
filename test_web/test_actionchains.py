from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_action:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip #不执行这个方法
    def test_clik(self):
        # self.driver.get("https://www.baidu.com/")
        a = self.driver.find_element(By.CSS_SELECTOR,'[class="title-content c-link c-font-medium c-line-clamp1"]')
        #导入actionchains包 ，传入driver
        action = ActionChains(self.driver)
        #添加事件，点击元素
        # action.click(a)
        action.click_and_hold(a)
        action.perform()
    def test_moveto(self):
        self.driver.get('https://www.baidu.com/')
        op = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(op)
        action.perform()

