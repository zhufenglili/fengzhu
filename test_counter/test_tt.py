class Test_0:
    def setup_class(self):
        print('类级别开始')

    def teardown_class(self):
        print("类级别结束")

    def seup(self):
        print("方法级别")

    def teardown(self):
        print("方法级别结束")