from time import sleep

from selenium.webdriver.common.by import By

from test_web.base import base


class Test_frame(base):
    def testwindow(self):
        self.driver.find_element_by_link_text("登录").click()
        # 打印当前浏览器窗口句柄,打印所有窗口是返回列表
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, '[class="pass-reglink pass-link"]').click()
        print(self.driver.current_window_handle)
        # 打印所有句柄窗口,所有窗口以列表返回
        print(self.driver.window_handles)
        #定义所有窗口
        window_1 = self.driver.window_handles
        sleep(3)
        #切换窗口switch ，获取所有窗口变量中切换的窗口
        self.driver.switch_to_window(window_1[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys('封枫讽凤')
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys('18887878789')
        #切换回上一个窗口，所有窗口的第一个窗口
        self.driver.switch_to_window(window_1[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys('15011591912')
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('lifengzhu1992')
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
