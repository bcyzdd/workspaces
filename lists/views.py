from django.shortcuts import render,redirect
from lists.models import Item

# Create your views here.

# def home_page(request):
#     # return render(request,'home.html')
#     #使用Django中的render函数构建HttpResponse，第一个参数为请求对象，
#     # 第二个是渲染模板，Django会自动搜索templates文件夹下，根据模板内容创建一个HttpResponse
#     # if request.method=='POST':
#     #     return HttpResponse(request.POST['item_text'])
#     # return render(request,'home.html')
#     # return render(request,'home.html',{
#     #     'new_item_text':request.POST.get('item_text',''),
#     # })
#     item=Item()
#     item.text=request.POST.get('item_text','')
#     item.save()
#
#     return render(request,'home.html',{
#         'new_item_text':item.text
#     })


# def home_page(request):
#     if request.method == 'POST':
#         new_item_text = request.POST['item_text']
#         Item.objects.create(text=new_item_text)
#     else:
#         new_item_text = ''
#     return render(request,'home.html',{
#         'new_item_text':new_item_text,
#     })
def home_page(request):
    if request.method=='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})