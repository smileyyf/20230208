# -*- coding: utf-8 -*-
import os
import sys

from common.times import dt_strftime
from common.readconfig import ReadConfig

class ConfigManager(object):
    BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    DRIVER_PATH = os.path.join(BASE_DIR,'driver')
    print('日志：',os.path.join(BASE_DIR, 'driver'))

    CHROME_PATH = os.path.join(DRIVER_PATH, 'chromedriver.exe')

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_locators')

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'report.html')

    # 测试输出目录
    OUTPUT_FILE = os.path.join(BASE_DIR, 'outputs')

    @property
    def screen_path(self):
        """截图目录，根据时间生成图片名"""
        screenshot_dir = os.path.join(self.OUTPUT_FILE, 'screen_capture')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        now_time = dt_strftime("%Y%m%d%H%M%S")
        screen_file = os.path.join(screenshot_dir, "{}.png".format(now_time))
        return now_time, screen_file

    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.OUTPUT_FILE, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime('%Y-%m-%d')))

    @property
    def ini_file(self):
        """配置文件地址"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file

    @property
    def venv(self):
        """获取当前执行环境"""
        ini = ReadConfig(self.ini_file)
        return ini.get_('VENV', 'venv')

    @property
    def url(self):
        """系统url"""
        ini = ReadConfig(self.ini_file)
        if self.venv == 'prod':
            return ini.get_('HOST', 'url')
        elif self.venv == 'pre':
            return ini.get_('HOST', 'url_pre')
        elif self.venv == 'test':
            return ini.get_('HOST', 'url_test')

    @property
    def username(self):
        """登录用户名"""
        ini = ReadConfig(self.ini_file)
        if self.venv == 'prod':
            return ini.get_('LOGIN', 'username')
        elif self.venv == 'pre':
            return ini.get_('PRE', 'username')
        elif self.venv == 'test':
            return ini.get_('TEST', 'username')

    @property
    def password(self):
        """登录密码"""
        ini = ReadConfig(self.ini_file)
        if self.venv == 'prod':
            return ini.get_('LOGIN', 'password')
        elif self.venv == 'pre':
            return ini.get_('PRE', 'password')
        elif self.venv == 'test':
            return ini.get_('TEST', 'password')

    # @property
    # def dingding(self):
    #     """获取钉钉消息发送配置"""
    #     ini = ReadConfig(self.ini_file)
    #     return ini.get_('DING', 'status')


cm = ConfigManager()
if __name__ == '__main__':
    print((lambda x: '生产环境' if x == 'prod' else '预发布环境' if x == 'pre' else '测试环境')(cm.venv))
    print(cm.url)