# -*- coding: utf-8 -*-
import base64
import sys
import time

import pytest
import allure
from py.xml import html
from selenium import webdriver
from common.logger import log
from config.conf import cm
from common.times import timestamp
from page_object.chaxunshuju import Search
# from page_object.loginpage import LoginPage
WIN = sys.platform.startswith('win')
# driver = webdriver.Chrome(cm.CHROME_PATH)
driver = webdriver.Chrome('C:\\Users\\叶玉飞\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')

@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    log.info('-----------正在执行测试用例开始的准备工作,打开浏览器-----------')
    driver.maximize_window()
    cc = Search(driver)
    cc.get_url(cm.url)
    def fn():
        driver.quit()
        log.info('-----------关闭浏览器-----------')

    request.addfinalizer(fn)

    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param
    item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot()
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)

def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)

def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


def pytest_html_report_title(report):
    report.title = "yyf平台UI自动化测试报告"


def pytest_configure(config):
    config._metadata.clear()
    config._metadata['测试项目'] = "YYF平台"
    config._metadata['测试地址'] = cm.url

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.clear()  # 清空summary中的内容
    # prefix.extend([html.p("所属部门: XX公司测试部")])

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    passed = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    failed = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    skipped = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    execute = passed + failed + skipped
    starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(terminalreporter._sessionstarttime)))
    timeout = round(timestamp() - terminalreporter._sessionstarttime, 2)
    try:
        sucess = str(round(len(terminalreporter.stats.get('passed', [])) / execute * 100, 2)) + '%'
    except ZeroDivisionError:
        sucess = '0.00%'
    result = {
        "总计用例数": terminalreporter._numcollected,
        "本次执行用例数": execute,
        '通过用例数': passed,
        '失败用例数': failed,
        '执行报错用例数': len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown']),
        '跳过的用例数': skipped,
        '成功率': sucess,
        # terminalreporter._sessionstarttime 会话开始时间
        '本次执行开始时间': starttime,
        '本次执行耗时': '{}s'.format(timeout)
    }
    print(result)
    # if result['failed'] or result['error']:
    env = (lambda x: '生产环境' if x == 'prod' else '预发布环境' if x == 'pre' else '测试环境')(cm.venv)
    # dingding = cm.dingding.lower()
    # if 'true'.__eq__(dingding):
    #     data = {"msgtype": "text",
    #             "text":
    #                 {
    #                     "content": "--代账UI自动化测试本次执行结果--"
    #                                "\n测试环境：{}".format(env) +
    #                                "\n执行测试用例数：{}".format(execute) +
    #                                "\n通过率：{}".format(sucess) +
    #                                "\n通过用例数：{}".format(passed) +
    #                                "\n失败用例数：{}".format(failed) +
    #                                "\n时间：{}".format(starttime) +
    #                                "\n耗时：{}s".format(timeout) +
    #                                "\n报告地址：http://10.83.1.43:8989/job/yzf_dz_ui_auto_pre/allure/#behaviors"
    #                 }
    #             }
    #     # DingTalkSend(data)


def _capture_screenshot():
    """截图保存为base64"""
    now_time, screen_file = cm.screen_path
    driver.save_screenshot(screen_file)
    allure.attach.file(screen_file, "失败截图{}".format(now_time), allure.attachment_type.PNG)
    with open(screen_file, 'rb') as f:
        imagebase64 = base64.b64encode(f.read())
    return imagebase64.decode()