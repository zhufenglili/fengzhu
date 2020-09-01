# main主要的
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_po.page import add_member
from test_po.page.add_member import Add_member
from test_po.page.basepage import Basepage
from test_po.page.contact_page import Contactpage
from selenium import webdriver


class Mainpage(Basepage):
    '''首页'''
    bastulr = ('https://work.weixin.qq.com/wework_admin/frame')
    contact = (By.CSS_SELECTOR, '[class="frame_nav"] a:nth-child(2)')

    def go_to_contact(self):
        '''跳转到通信录'''
        self.find(*self.contact).click()
        # 实例化Contact类，表示业务直接逻辑关系转换
        return Contactpage(self._driver)

    def go_to_add_member(self):
        ''' 跳转到添加成员'''
        # 定位添加员工元素跳转
        self._driver.find_element(By.CSS_SELECTOR, '[node-type="addmember"]').click()
        return Add_member(self._driver)
