from asyncio import sleep

import allure


@allure.feature('登录模块')
class Test_1:
    @allure.story("子功能模块")

    def test_a(self):
        with allure.step('点击什么之后登录失效'):
            assert 1 == 1
            sleep(0.5)


    def test_aa(self):
        assert 2 == 3
        sleep(0.5)
    def test_aa(self):
        assert 3== 3
        sleep(0.5)