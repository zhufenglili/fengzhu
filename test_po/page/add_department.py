from selenium.webdriver.common.by import By

from test_po.page.basepage import Basepage


from test_po.page.report import Report


class add_department(Basepage):
    '''部门'''
    _adddepartment = (By.CSS_SELECTOR, '[class="qui_inputText ww_inputText"]')
    _adddepartment2 = (By.CSS_SELECTOR, '.js_toggle_party_list')
    _adddepartment3 = (By.CSS_SELECTOR, '[class="jstree-anchor"]')
    _save = (By.CSS_SELECTOR, '[class="qui_dialog_foot ww_dialog_foot"] a:nth-child(1)')
    _cancel = (By.CSS_SELECTOR, '[class="qui_dialog_foot ww_dialog_foot"] a:nth-child(2)')

    def add_department(self, ooo):
        '''添加部门'''
        self.find(*self._adddepartment).send_keys(ooo)
        self.find(*self._adddepartment2).click()  # 所属部门按钮
        self.find(*self._adddepartment3).click()  # 所属公司
        return self

    def department_save(self):
        '''确定按钮'''
        from test_po.page.contact_page import Contactpage
        self.find(*self._save).click()  # 点击确定按钮
        return Contactpage(self._driver)

    def department_cancel(self):
        '''取消按钮'''
        from test_po.page.contact_page import Contactpage
        self.find(*self._cancel).click()  # 点击取消按钮
        return Contactpage(self._driver)