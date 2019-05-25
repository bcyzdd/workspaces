# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 下午5:33
# @Author  : Mat
# @Email   : bcy_51testing@163.com
# @File    : functional_tests.py
# @Software: PyCharm
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT=2

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        start_time=time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError,WebDriverException) as e:
                if time.time()-start_time>MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')


        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')


        self.fail('Finish the test!')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')

        ##打开一个新浏览器
        ##确保用户信息不会从cookie中泄露出去
        self.browser.quit()
        self.browser=webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        fancis_list_url=self.browser.current_url
        self.assertRegex(fancis_list_url,'/lists/.+')
        self.assertNotEqual(fancis_list_url,edith_list_url)

        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
