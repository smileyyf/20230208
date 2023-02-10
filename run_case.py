# -*- coding: utf-8 -*-

import os
import sys
import pytest
from common.readconfig import *
from config.conf import cm
from common.times import sleep


pytest.main(['--clean-alluredir', '-v', './TestCase/', '--alluredir', './allure-results'])