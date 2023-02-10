# -*- coding: utf-8 -*-
import logging
import os
import time
Time = time.strftime('%Y-%m-%d',time.localtime())
CURRENT_PATH =os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(os.path.dirname(CURRENT_PATH),'log')

class Log:
    def __init__(self):
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        self.log_name = os.path.join(LOG_PATH,'%s.log'%time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger()

        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            fh = logging.FileHandler(self.log_name,'a',encoding='utf-8')
            fh.setLevel(logging.INFO)

            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)


            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)
            # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

log = Log().logger

if __name__ == '__main__':
    log.info('hello world')