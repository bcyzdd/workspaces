# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 下午6:41
# @Author  : Mat
# @Email   : bcy_51testing@163.com
# @File    : tests.py
# @Software: PyCharm
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
MAX_WAIT=10 #通过常量设置最长等待时间

class NewVistorTest(LiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def wait_for_row_in_list_table(self,row_text):
        start_time=time.time()
        while True:#循环一直运行，直到两个出口中的一个为止
            try:
                table=self.browser.find_element_by_id('id_list_table')
                rows=table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return #如果运行顺利通过了，就退出函数，跳出循环 第一个出口
            except (AssertionError,WebDriverException)as e: #捕获异常，就等待一小段时间然后再循环
                if time.time()-start_time>MAX_WAIT: #第二个出口 执行到此处，说明代码已经不断抛出异常，已经超时
                    raise e
                time.sleep(0.5)
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        header_text=self.browser.find_element_by_tag_name('h1').text
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('1：Buy peacock feathers')
        inputbox = self.browser.find_element_by_id('id_new_item')
        time.sleep(1)
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('Fish the test!!')

    def test_can_start_a_list_for_one_user(self):
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1:Buy peacock feathers')
    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1：Buy peacock feathers')

        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/lists.+')

