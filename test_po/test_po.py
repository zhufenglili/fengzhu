from test_po.page import main_page
from test_po.page.main_page import Mainpage


class Test_add_member():
    def setup_class(self):
        '''初始化main页面'''
        self.main = Mainpage()  # 这里实例化要带括号，调用mainpage模块

    def test_add_member(self):
        '''从首页进入添加成员页面进行添加成员-保存-返回通讯录-打印姓名列表'''
        namelist = self.main.go_to_add_member().add_member('小李', '444',
                                                           '13613614043').seve_meber().get_member_list()  # 保存
        assert '小李' in namelist

    def test_add_member_fail(self):
        '''失败案例'''
        namelist = self.main.go_to_add_member().add_member('小张', '444',
                                                           '13613614043').cancel_meber().get_member_list()  # 保存
        print(namelist)
        assert '小张' not in namelist

    def test_contact_member(self):
        '''从首页-通讯录-添加成员-添加'''
        self.main.go_to_contact().go_to_add_member().add_member('小df', '3343',
                                                                '15011691912').seve_meber().get_member_list()
    def test_add_department(self):
        '''首页-通讯录-添加部门-添加-保存-返回列表'''
        department = self.main.go_to_contact().go_to_department().add_department('测试公司').department_save().get_department_list()
        assert '测试公司' in department
    def test_cancel_deparment(self):
        '''首页-通讯录-添加部门-添加-取消'''
        deprtment_list= self.main.go_to_contact().go_to_department().add_department('测试公司1').department_cancel().get_department_list()
        assert '测试公司1' not in deprtment_list

    def teardown(self):
        self.main._driver.quit()
