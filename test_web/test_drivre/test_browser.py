import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_l:

    def setup(self):

        option=Options()
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        option.debugger_address='127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')


    def test_cookie(self):
        # # 获取Ccookie值
        # cookie = self.driver.get_cookies()
        # print(cookie)
        #带有登录信息的COOKIE
        cookie = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852956660879'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '5_Nt-0P2oJYuo1I53GrVGE1HKYPKr0YlGD0tn3L9uEBl71F06FgNT9pGYldsL6MyyGqdqASMG5XPLB1cSYs-v5BC_A1egvTVWJ8i9o9QdkR4jsCLsHbHPDGJqX61-LFs4mtuoLSSYebaAz2y207Q3w7298IL9ZUxxyaRAVkDcC6hGqknwuVXwwNI-n45rERYQSwP_oFchutSwTQ6ViPqBxaHn6NF-2hnTP7kXhQVVLepbWjrvqbypvv_a85hwamN9P19Fug0mGLR37eZ3OAeNA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852956660879'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598333937'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '20682479281592452'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629869937, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598267201,1598333937'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598365471, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '38ig9rj'}, {'domain': '.qq.com', 'expiry': 1598420352, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.611438240.1598267201'}, {'domain': '.qq.com', 'expiry': 1613388747, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': True, 'value': 'E1J5S851q8Z5k2T7L4p7r0c0x5'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'R1p6utMjZ4A7LBxfhA-nlesGcdSE3bnelf7diwj74wYKtFLhVX0m0KOKoPBHXIje'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629803190, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325006158329'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '4722454528'}, {'domain': '.qq.com', 'expiry': 1613388745, 'httpOnly': False, 'name': 'LW_uid', 'path': '/', 'secure': True, 'value': 'I1y598v1d8S592I7s4I5I8u4l4'}, {'domain': '.qq.com', 'expiry': 1613388745, 'httpOnly': False, 'name': 'LW_sid', 'path': '/', 'secure': True, 'value': 'S1P5J8l1M8P542X7B4r5B8F4Y2'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5476992'}, {'domain': '.qq.com', 'expiry': 2147484152, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': '0eg4jz8WX5'}, {'domain': '.qq.com', 'expiry': 2147484162, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '6f36a4dd40a440ec60fbf11cab91586e1d89521884581b92c8c5a5edc6bb53af'}, {'domain': '.qq.com', 'expiry': 1661405952, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1039098940.1598267201'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '5404719705'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600926742, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        for i in cookie:
            #把cookie遍历到当前页面中
            self.driver.add_cookie(i)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
    def test_clent(self):
        # self.driver.find_element_by_link_text('添加成员').click()
          self.driver.find_element_by_link_text('导入通讯录').click()
        #上传文件
          self.driver.find_element_by_id("js_upload_file_input").send_keys('D:\ll.xls')
        # 获取文件的文本属性,与文件名称进行断言
          assert 'll.xls'== self.driver.find_element_by_id("upload_file_name").text
