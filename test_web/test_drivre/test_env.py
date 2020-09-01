import os

from selenium import webdriver
class Test_1:
    def setup(self):
       browser = os.getenv('browser')
       if browser == 'Chrome':
           self.driver = webdriver.Chrome()