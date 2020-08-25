from selenium import  webdriver
class Tests:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
    def teardown(self):
        self.driver.quit()

    def test_11(self):
        pass