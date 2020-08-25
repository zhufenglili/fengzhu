from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_get:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_1(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('李枫竹')
        self.driver.find_element(By.XPATH,"//*[@id='1']//a").click()

        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="s_btn"]')))
        self.driver.find_element(By.CSS_SELECTOR,'[class="s_tab_item s_tab_webpage"]').click()
