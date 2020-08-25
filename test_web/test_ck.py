import shelve
from time import sleep

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By


class Testl:
    def setup(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown(self):
    #     self.driver.quit()

    def test_cookies(self):
        # 获取cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        f = shelve.open('./cc/cookies')
        #取出f文件的key
        cookies = f['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
                #把cookie添加到本地driver
            self.driver.add_cookie(cookie)
            # 再次访问当前页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)
    def  test_login(self):
        sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        sleep(3)