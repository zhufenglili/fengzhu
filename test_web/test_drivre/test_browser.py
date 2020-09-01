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


    def test_shelve(self):
        #打开数据库
        f = shelve.open('./myf/cookis')
        cookie = f['c'] #文件F中的C KYE值 赋值给cookie
        for i in cookie:
            # if 'expiry' in cookie.keys():
            #     cookie.pop('expiry')
            # 把cookie遍历到当前页面中
            self.driver.add_cookie(i)
        # 再次访问网页
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # # 获取Ccookie值
        # cookie = self.driver.get_cookies()
        # print(cookie)
        #带有登录信息的COOKIE
        #shelvepython提供的模块
        #创建一个库
        # f = shelve.open('./myf/cookis')
        # #创建一个key把cookie值放进去
        # f['c'] = cookie
        # f.close()

    def test_clent(self):
        # _by_link_text('添加成员').click()
          _by_link_text('导入通讯录').click()
        #上传文件
          self.driver.find_element_by_id("js_upload_file_input").send_keys('D:\ll.xls')
        # 获取文件的文本属性,与文件名称进行断言
          assert 'll.xls'== self.driver.find_element_by_id("upload_file_name").text
