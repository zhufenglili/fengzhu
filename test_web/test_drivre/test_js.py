from time import sleep

import pytest
from selenium.webdriver.common.by import By

from test_web.test_drivre.myf.aa import aa


class Test_js(aa):
    @pytest.mark.skip
    def test_js_scrool(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys('软件测试')
        sleep(3)
        execute = self.driver.execute_script('return document.getElementById("su")')
        execute.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'[class="n"]').click()
        sleep(3)
        # for a in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(a))
        print(self.driver.execute_script( 'return document.title;return JSON.stringify(performance.timing)'))
    def test_time(self):
        self.driver.get('https://www.12306.cn/index/')
        # time=self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        # self.driver.execute_script('document.getElementById("train_date").value="1999-05-12"')
        # sleep(10)
        time =self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script(' document.getElementById("train_date").value="1999-05-12"')
        sleep(3)