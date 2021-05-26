"""L
@author:  伍辉
@data: 2021-5-26
@function python 基本用法
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.lggs_page import LggsPage

class TestLggsLogin:
    '''理工亘舒云监控平台登录测试'''

    def test_lggs_loginAdmin_case(self, browser, base_url):
        """
        名称：理工亘舒云监控平台admin账号登录
        步骤：
        1、打开云监控平台
        2、输入用户名密码
        3、点击登录按钮
        检查点：
        * 检查登录后页面右上角是否显示账号名称
        """
        page=LggsPage(browser)
        page.get(base_url)
        page.loginUser_input='admin'
        page.loginPasswd_input='123456'
        page.login_button.click()
        sleep(2)
        assert page.user_span.text=='管理员'

    def test_lggs_loginYYJG_case(self, browser, base_url):
        """
        名称：理工亘舒云监控平台运营机构账号登录
        步骤：
        1、打开云监控平台
        2、输入用户名密码
        3、点击登录按钮
        检查点：
        * 检查登录后页面右上角是否显示账号名称
        """
        page=LggsPage(browser)
        page.get(base_url)
        page.loginUser_input='13900000001'
        page.loginPasswd_input='123456'
        page.login_button.click()
        sleep(2)
        assert page.user_span.text=='自动化测试运营机构账号'

    def test_lggs_loginQSF_case(self, browser, base_url):
        """
        名称：理工亘舒云监控平台起送方账号登录
        步骤：
        1、打开云监控平台
        2、输入用户名密码
        3、点击登录按钮
        检查点：
        * 检查登录后页面右上角是否显示账号名称
        """
        page=LggsPage(browser)
        page.get(base_url)
        page.loginUser_input='13900000002'
        page.loginPasswd_input='123456'
        page.login_button.click()
        sleep(2)
        assert page.user_span.text=='qisong'

    def test_lggs_loginPSF_case(self, browser, base_url):
        """
        名称：理工亘舒云监控平台配送方账号登录
        步骤：
        1、打开云监控平台
        2、输入用户名密码
        3、点击登录按钮
        检查点：
        * 检查登录后页面右上角是否显示账号名称
        """
        page=LggsPage(browser)
        page.get(base_url)
        page.loginUser_input='13900000003'
        page.loginPasswd_input='123456'
        page.login_button.click()
        sleep(2)
        assert page.user_span.text=='peisongWeb'

    def test_lggs_loginJSF_case(self, browser, base_url):
        """
        名称：理工亘舒云监控平台接收方账号登录
        步骤：
        1、打开云监控平台
        2、输入用户名密码
        3、点击登录按钮
        检查点：
        * 检查登录后页面右上角是否显示账号名称
        """
        page=LggsPage(browser)
        page.get(base_url)
        page.loginUser_input='13900000005'
        page.loginPasswd_input='123456'
        page.login_button.click()
        sleep(2)
        assert page.user_span.text=='jieshou'

    def test_lggs_loginERR_case(self, browser, base_url):
        """
        名称：理工亘舒云监控平台错误账号登录
        步骤：
        1、打开云监控平台
        2、输入用户名密码
        3、点击登录按钮
        检查点：
        * 检查登录后页面右上角是否显示账号名称
        """
        page=LggsPage(browser)
        page.get(base_url)
        page.loginUser_input='13900000005'
        page.loginPasswd_input='12345'
        page.login_button.click()
        sleep(2)
        assert page.user_span.text=='jieshou'

if __name__ == '__main__':
    #pytest.main(["-v", "-s", "test_lggsLogin.py"])
    pytest.main(["-v", "-s", "test_lggsLogin.py::TestLggsLogin::test_lggs_loginERR_case"])