from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# 登录复用浏览器初始化
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:
    bastulr = ''

    def __init__(self, driver_base=None):
        if driver_base is None:  # 如果driver_base是0不存在，就复用下面浏览器
            option = Options()
            option.debugger_address = ('127.0.0.1:9222')
            self._driver = webdriver.Chrome(options=option)
        else:
            self._driver: WebDriver = driver_base  # 否则driver=driver_base 为0
        if self.bastulr != '':  # 如果bastulr不是空的，driver获取地址
            self._driver.get(self.bastulr)
            self._driver.implicitly_wait(5)


    def find(self, by, value):
        '''封装元素'''
        return self._driver.find_element(by, value)

    def wait_chlicabel(self, elment):
        '''显示等待元素可被点击'''
        return WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(elment))
