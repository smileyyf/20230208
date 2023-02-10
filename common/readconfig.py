# -*- coding: utf-8 -*-
import configparser
import os

class ReadConfig(object):

    def __init__(self,ini_file):
        self.config = configparser.RawConfigParser()
        self.ini_file = ini_file
        self.config.read(self.ini_file,encoding='utf-8')

    def get_(self,section,option):
        return self.config.get(section,option)

    def set_(self,section,option,value):
        self.config.set(section,option,value)

        with open(self.ini_file,'w') as f:
            self.config.write(f)