# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 下午6:41
# @Author  : Mat
# @Email   : bcy_51testing@163.com
# @File    : functional_tests.py
# @Software: PyCharm
from selenium import webdriver

browser=webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
