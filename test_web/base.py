from selenium import webdriver
class base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown(self):
    #     self.driver.quit()