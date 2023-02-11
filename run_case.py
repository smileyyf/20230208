# -*- coding: utf-8 -*-

import os
import sys
import pytest
from common.readconfig import *
from config.conf import cm
from common.times import sleep


pytest.main([ '-v', './TestCase/', '--alluredir', './allure-results'])
os.system("allure generate ./allure-results -o  ./report --clean")