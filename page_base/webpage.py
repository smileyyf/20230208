# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from common.logger import log
from common.times import sleep

class WebPage(object):
    """ selenium基类"""

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver,self.timeout)

    def get_url(self,url):
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        self.driver.refresh()
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    def get_ele(self,loc):
        """查找元素"""
        # 这里使用的是find_element查找单个元素,这里需要传入的是一个表达式,需要告诉driver对象使用的是什么定位方法,以及元素定位!
        # By是继承了selenium里面的8大定位方法,所以框架里操作元素的皆是By.XPATH或者By.id等等
        # 同时因为需要传入的是一个表达式,而By.XPATH是一个元组,这里做了解包处理
        ele = self.driver.find_element(*loc)
        return ele

    def send_key(self,loc,txt):
        self.get_ele(loc).send_keys(txt)


    def input_text(self,loc,txt):
        sleep(0.5)
        ele =self.get_ele(loc)
        ele.clear()
        log.info("清空文本")
        ele.send_keys(txt)
        log.info("输入文本:{}".format(txt))

    def click_key(self,loc):
        self.get_ele(loc).click()
        sleep()
        log.info("点击元素:{}".format(loc))

    def click_ele(self, loc):
        """ElementClickInterceptedException处理点击"""
        # self.driver.execute_script("arguments[0].click();", self.get_ele(loc))
        ele = self.get_ele(loc)
        webdriver.ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        sleep()
        log.info("点击元素:{}".format(loc))

    def get_ele_text(self, loc):
        """获取当前的text"""
        _text = self.get_ele(loc).text
        log.info('获取文本成功:{}'.format(_text))
        return _text

    def  get_ele_attribute(self, loc, attribute_name):
        """获取元素属性"""
        ele = self.get_ele(loc)
        value = ele.get_attribute(attribute_name)
        log.info('获取属性成功:{}'.format(value))
        return value

    def mouse_hover(self, loc):
        """鼠标悬停"""
        ele = self.get_ele(loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        log.info('鼠标悬停成功:{}'.format(loc))

    def wait_ele_click(self, loc):
        """等待可点击元素"""
        WebDriverWait(self.driver, timeout=20).until(EC.element_to_be_clickable(loc))
        log.info('等待可点击元素:{}'.format(loc))

    def switch_to_iframe(self, loc):
        """进入iframe嵌套页面"""
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        log.info('进入嵌套页面成功:{}'.format(loc))

    def switch_to_return(self):
        """退出iframe嵌套"""
        # self.driver.switch_to_default_content()
        self.driver.switch_to.parent_frame()

    def get_cur_handle(self):
        """获取当前窗口句柄"""
        jb=self.driver.window_handles
        self.driver.switch_to_window(jb[-1])

    def click_wait_ele(self, loc):
        """等待可点击元素出现并点击"""
        self.wait_ele_click(loc)
        self.get_ele(loc).click()
        log.info('点击元素:{}'.format(loc))

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    @property
    def get_title(self):
        """获取页面title"""
        return self.driver.title

        # 对浏览器的操作
        def refresh_brower(self):
            """刷新页面F5"""
            self.driver.refresh()
            self.driver.implicitly_wait(30)

        def close_brower(self):
            """关闭浏览器当前窗口"""
            self.driver.close()
            self.driver.implicitly_wait(30)

        def forward_brower(self):
            """关闭浏览器当前窗口"""
            self.driver.forward()
            self.driver.implicitly_wait(30)

if __name__ == '__main__':
    pass