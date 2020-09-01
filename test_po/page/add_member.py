# member成员
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_po.page.basepage import Basepage
from test_po.page.contact_page import Contactpage


class Add_member(Basepage):
    '''添加成员页'''
    _cancel = (By.CSS_SELECTOR, '[node-type="cancel"]')
    _save = (By.CSS_SELECTOR, '[class="qui_btn ww_btn js_btn_save"]')
    _cancel_add = (By.CSS_SELECTOR, '.js_btn_cancel')

    def add_member(self, name, acctid, add_phone):
        '''添加成员'''
        self._driver.find_element_by_id("username").send_keys(name)#参数变量 姓名
        self._driver.find_element_by_id("memberAdd_acctid").send_keys(acctid)#序号
        self._driver.find_element_by_id('memberAdd_phone').send_keys(add_phone)#手机号
        return self   #填写完毕，停留在添加成员页，可继续调用其他方法


    def seve_meber(self):
        '''保存按钮'''
        self.find(*self._save).click() #点击保存按钮
        return Contactpage(self._driver)  # 保存成功返回通讯录页面


    def cancel_meber(self):
        '''取消按钮'''
        self.find(*self._cancel_add).click()#点击取消按钮
        self.wait_chlicabel(self._cancel) #调用显示等待，知道元素出现进行点击
        self.find(*self._cancel).click() # 确定取消
        return Contactpage(self._driver) # 取消后返回通讯录页面
