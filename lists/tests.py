from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
# Create your tests here.


class HomePageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found=resolve('/')
    #     self.assertEqual(found.func,home_page)

    # def test_home_page_returns_correct_htmL(self):
    #     # request=HttpRequest()
    #     # response=home_page(request)
    #     response=self.client.get('/')           #检测的原生方式
    #     html=response.content.decode('utf-8')
    #
    #     expected_html=render_to_string('home.html') #测试是否正确渲染模板，然后与视图返回的结果做对比 自定义检测，万能模式
    #     self.assertEqual(html,expected_html)
    #
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>',html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #
    #     self.assertTemplateUsed(response,'home.html') #测试是否正确渲染模板，然后与视图返回的结果做对比   检测的原生方式
    #
    #     self.assertEqual(response,'wrong.html')
    #
    def test_users_home_template(self):
        response=self.client.get('/')
        self.assertTemplateUsed(response,'home.html')