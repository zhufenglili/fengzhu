# 通讯录
from time import sleep

from selenium.webdriver.common.by import By

from test_po.page.add_department import add_department
from test_po.page.basepage import Basepage


class Contactpage(Basepage):
    '''通讯录'''
    _add_member = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    _department = (By.CSS_SELECTOR,'.js_create_dropdown')
    _add_department =(By.CSS_SELECTOR,'.js_create_party')
    # _get_department=(By.CSS_SELECTOR,'[class="jstree-wholerow"]')
    # _dd = (By.CSS_SELECTOR,'.jstree-clicked')

    def go_to_add_member(self):
        '''点击添加成员，跳转到添加成员'''
        from test_po.page.add_member import Add_member  # 解决循环导入方式，放入方法中
        self.wait_chlicabel(self._add_member)  # js元素慢 ，可以调用显示等待
        self.find(*self._add_member).click()  # 点击’添加成员‘元素封装到配置中，直接调用方法名使用，解包传参
        return Add_member(self._driver)  # 返回添加成员页

    def get_member_list(self):
        '''获取通讯录列表'''
        # 拿到通讯录姓名列表 必须是find_elments才能取到列表
        a_list = self._driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

        # 遍历通讯录姓名列表
        print(a_list)
        return [name.text for name in a_list]

    def go_to_department(self):
        '''跳转到部门'''
        self.find(*self._department).click()#点击加号按钮
        self.find(*self._add_department).click()
        return add_department(self._driver)

    def get_department_list(self):
        '''获取部门列表'''

        list_1=self._driver.find_elements(By.CSS_SELECTOR,'[role="treeitem"] a:nth-child(3)')
        return [name_1.text for name_1 in list_1]
