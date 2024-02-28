from django.shortcuts import render, redirect

# Create your views here.
#显示主页面
from django.urls import reverse

from smallapp.models import *
from django.http import HttpResponse, JsonResponse
import json

#主页
def index(request):

    return render(request,'smallapp/home/index.html')



#注册页面
def register(request):

    return render(request, 'smallapp/home/register.html')

#保存注册用户的信息peoregister
def peoregister(request):
    # 判断用户时候post模式提交
    if request.method != 'POST':
        return render(request, 'smallapp/home/register.html')
    # 获取前端传送数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    sex = request.POST.get('sex')
    date = request.POST.get('date')
    # 创建一个对象
    user = Peoples()
    user.username = username
    user.password = password
    user.sex = sex
    user.createtime = date
    user.is_delete = 1
    user.save()
    return redirect(reverse('index'))


def userContrast(request,name):

    alldata = Peoples.objects.all()
    print(len(alldata))
    return HttpResponse(json.dumps(alldata))

#登陆页面
def login01(request):

    return render(request, 'smallapp/home/login01.html')


#登录操作
def do_login(request):
    username=request.POST.get('username')
    pswd=request.POST.get('pswd')
    print('前端密码'+pswd)
    print('前端用户名'+username)
    try:
        #查找到该用户的对象
        print('1')
        obj=Peoples.objects.get(username=username) #没错误说明查到了该对象
        print('2')
        print('数据库用户名'+obj.username)
        if obj.password==pswd:
            print('3')
            request.session['username']=username#将该对象的密码与前台密码比较
            print('4')
            print('数据库密码' + obj.password)
            # con={
            #     'username':username
            # }
            return redirect(reverse('index'))
        else:
            return render(request, 'smallapp/home/login01.html')
    except :
        return render(request,'smallapp/home/login01.html')

#文章页面
def wz(request):

    return render(request, 'smallapp/home/wz/文章.html')

#文章页面
def wz01(request):

    return render(request, 'smallapp/home/wz/文章01.html')
#文章页面
def wz02(request):

    return render(request, 'smallapp/home/wz/文章02.html')
#文章页面
def wz03(request):

    return render(request, 'smallapp/home/wz/文章03.html')
#文章页面
def wz04(request):

    return render(request, 'smallapp/home/wz/文章04.html')



#资讯页面
def zx(request):

    return render(request, 'smallapp/home/zx/资讯.html')
#资讯页面
def zx01(request):

    return render(request, 'smallapp/home/zx/资讯01.html')
#资讯页面
def zx02(request):

    return render(request, 'smallapp/home/zx/资讯02.html')
#资讯页面
def zx03(request):

    return render(request, 'smallapp/home/zx/资讯03.html')
#资讯页面
def zx04(request):

    return render(request, 'smallapp/home/zx/资讯04.html')


#About us页面
def aboutUs(request):

    return render(request, 'smallapp/home/About us.html')



