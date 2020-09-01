from selenium import webdriver
class aa :
    def setup(self):
        self.driver =webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()