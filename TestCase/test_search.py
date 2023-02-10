# -*- coding: utf-8 -*-

import allure
import pytest
import time
from page_locators.baidu_search import Chaxun as  cx
from page_object.chaxunshuju import Search
from selenium import webdriver
from page_base import webpage

@allure.epic("ui自动化测试报告")
@allure.feature("cx")
class TestChaXun:
    @allure.story("查询")
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_suitcase_001(self,drivers):

        ser = Search(drivers)

        ser.input_xx('测试')
        time.sleep(2)
        ser.mouse_click()
        time.sleep(2)

        assert  1 == 1

if __name__ == '__main__':
    pytest.main(['.'])


