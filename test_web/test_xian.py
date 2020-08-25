from time import sleep

from selenium.webdriver import ActionChains

from test_web.base import base

#继承类
class Test_browser(base):
    def test_xianx(self):
        #实例化action
        # action = ActionChains(self.driver)
        # #元素变量
        # o = self.driver.find_element_by_id("s-usersetting-top")
        # #鼠标移动指定的位置
        # action.move_to_element(o)
        # #执行
        # action.perform()
        # sleep(3)
        #获取元素
        a = self.driver.find_element_by_id("s-usersetting-top")
        #获取元素属性
        assert 's-top-right-text c-font-normal c-color-t'== a.get_attribute("class")