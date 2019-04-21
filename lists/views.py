from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    # return render(request,'home.html')
    #使用Django中的render函数构建HttpResponse，第一个参数为请求对象，
    # 第二个是渲染模板，Django会自动搜索templates文件夹下，根据模板内容创建一个HttpResponse
    if request.method=='POST':
        return HttpResponse(request.POST['item_text'])
    return render(request,'home.html')

