# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 下午6:41
# @Author  : Mat
# @Email   : bcy_51testing@163.com
# @File    : functional_tests.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import  unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_for_row_in_list_table(self,row_text):
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])



    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('To-Do',header_text)
        # inputbox=self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),'Enter a to-do item'
        # )
        # # inputbox.send_keys('Buy peacock feathers')
        # inputbox.send_keys('Use peacock feathers to make a fly')
        # inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)


        inputbox=self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # table=self.browser.find_element_by_id('id_list_table')
        # rows=table.find_elements_by_tag_name('tr')
        # # self.assertTrue(
        #     any(row.text=='1:Buy peacock feathers' for row in rows),
        #     # 'New to-do item did not appear in table' #将自定义的错误消息传给unittest中的大多数assertx方法
        #     f"New to-do item did not appear in table. Contents were:\n{table.text}"
        # )
        # self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        #
        # self.assertIn('2: Use peacock feathers to make a fly',[row.text for row in rows]
        # )

        self.fail('Fish the test!!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')
