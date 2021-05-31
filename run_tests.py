# coding=utf-8
import os
import time
import logging
import pytest
import click
import yagmail as yagmail
import erros
from conftest import REPORT_DIR
from config import RunConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py  (回归模式，生成HTML报告)
  > python run_tests.py -m debug  (调试模式)
'''


def init_env(new_report):
    """
    初始化测试报告目录
    """
    os.mkdir(new_report)
    os.mkdir(new_report + "/image")
    
#把测试报告作为附件发送到指定邮箱
def send_mail(report):
 yag = yagmail.SMTP(user="wuhui@lggs.tech",
 password="Admin@55555",
 host='smtp.lggs.tech',)
 subject = "理工亘舒云监控平台ui自动化测试报告"
 contents = "<b>理工亘舒UI自动化测试过程中出现以下报错信息:</b>"
 mail_tail = "<p style=\"color:blue\">测试详情请参考自动化测试报告！</p>"

 # 添加错误列表数据
 for error in erros.errors:
     contents = contents + '<p style=\"color:red\">' + str(error) + '</p>'
 contents+=mail_tail
 yag.send('wuhui@lggs.tech', subject, contents, report)
 print('邮件已发送')

@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)
        init_env(RunConfig.NEW_REPORT)
        html_report = os.path.join(RunConfig.NEW_REPORT, "report.html")
        xml_report = os.path.join(RunConfig.NEW_REPORT, "junit-xml.xml")
        pytest.main(["--capture=sys", "-v", RunConfig.cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun
                     ])
        logger.info("运行结束，生成测试报告♥❤！")

        # 发送报告邮件
        if(erros.is_error()):
            send_mail(html_report)

    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
