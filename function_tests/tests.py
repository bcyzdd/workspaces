# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 下午6:41
# @Author  : Mat
# @Email   : bcy_51testing@163.com
# @File    : tests.py
# @Software: PyCharm
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVistorTest(LiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_for_row_in_list_table(self,row_text):
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        header_text=self.browser.find_element_by_tag_name('h1').text
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('1:Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        inputbox = self.browser.find_element_by_id('id_new_item')
        time.sleep(1)
        inputbox.send_keys('2: Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('Fish the test!!')

