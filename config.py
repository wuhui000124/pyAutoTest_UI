import os
import random

PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    #运行整个测试用例目录
    cases_path = os.path.join(PRO_PATH, "test_dir")

    # 运行测试用例单个文件
    #cases_path = os.path.join(PRO_PATH, "test_dir", "test_aLogin.py")

    # 运行测试用例单个文件下单个用例
    #cases_path = os.path.join(PRO_PATH, "test_dir", "test_emqManage.py::TestempManage::test_input_emq")

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "https://cloudtest.gdgs.tech/"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None

    #生成15位随机冷箱识别码
    clientId="".join(random.choice("0123456789") for i in range(15))
