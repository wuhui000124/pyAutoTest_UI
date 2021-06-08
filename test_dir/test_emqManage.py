"""
@author:  伍辉
@data: 2021-6-04
@function python 基本用法
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath
import erros
from page.lggs_page import LggsPage
from config import RunConfig
sys.path.insert(0, dirname(dirname(abspath(__file__))))

class TestempManage:
    '''云监控系统管理员冷箱管理功能测试'''
    def test_input_emq(self, browser, base_url):
        """
        名称：理工亘舒云监控平台冷箱录入测试
        步骤：
        1、登录admin管理员账号
        2、点击冷箱管理-录入新冷箱
        3、录入冷箱信息后点击录入冷箱按钮
        检查点：
        * 检查录入后页面是否显示录入的冷箱信息
        """

        #登录admin管理员账号
        page = LggsPage(browser)
        page.get(base_url)
        page.loginUser_input = 'admin'
        page.loginPasswd_input = '123456'
        page.login_button.click()
        sleep(2)

        #录入冷箱
        page.empManage_span.click()
        page.inputEmp_button.click()

        #使用随机生成的15位冷箱识别码
        page.clientId_input=RunConfig.clientId

        page.empNum_select.click()
        page.empNum_option.click()

        # 使用随机生成的15位冷箱识别码
        page.Bluetooth_input=RunConfig.clientId

        page.calendar_button.click()
        page.calendar_select.click()
        page.productNum_input='ui自动化测试生产批号'
        page.productHome_input='ui自动化测试生产厂家'
        page.version_input='1.0.1'
        page.yunyJg_select.click()
        page.yunyJg_option.click()
        page.addEmp_button.click()
        sleep(3)

        #判断冷箱是否录入成功
        pytest.assume(page.emp_local.text == RunConfig.clientId)
        if (page.emp_local.text != RunConfig.clientId):
            erros.errors_add('冷箱列表未找到冷箱，冷箱录入失败')


if __name__ == '__main__':
    #pytest.main(["-v", "-s", "test_aLogin.py"])
    pytest.main(["-v", "-s", "test_emqManage.py::TestempManage::test_input_emq"])