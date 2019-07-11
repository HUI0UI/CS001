import allure
import pytest


class Test01():
    @allure.step(title="正在执行登陆操作")
    def test01(self):
        print('test001被执行')

    @allure.step(title="正在执行退出操作")
    def test02(self):
        print('test002被执行')

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        allure.attach('描述','test03正在被执行')
        print('test003被执行')

    def test04(self):
        allure.attach('描述','')
        print('test004被执行')

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test05(self):
        with open('./image/fail.png','rb')as f:
            allure.attach('失败原因:',f.read(),allure.attach_type.PNG)

            # print('test05被执行')