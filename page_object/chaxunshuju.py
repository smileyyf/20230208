# -*- coding: utf-8 -*-

from page_base.webpage import WebPage

from page_locators.baidu_search import Chaxun as cx

class Search(WebPage):

    def input_xx(self,content):
        self.input_text(cx.shuru,content)

    def mouse_click(self):

        self.click_key(cx.tj)