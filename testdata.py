# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.find_element(By.XPATH,('//*[@id="kw"]')).send_keys('cs')
time.sleep(3)