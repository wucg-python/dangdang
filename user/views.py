from django.db import transaction
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from index.models import TUser
from captcha.image import ImageCaptcha
import random,string

# Create your views here.


def login(request):
    w = request.GET.get('w',5)
    level = request.GET.get('level')
    id = request.GET.get('id')
    num = request.GET.get('num')
    if request.COOKIES.get('name'):
        request.session['is_login'] = request.COOKIES.get('name')
        return redirect('index:index')
    return render(request,'login.html',{'w':w,'level':level,'id':id,'num':num})


def login_logic(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    checked = request.POST.get('checked')
    with transaction.atomic():
        if TUser.objects.filter(name=name,password=password):
            request.session['is_login'] = name
            if checked=='true':
                res = HttpResponse('ok')
                res.set_cookie('name',name,max_age=7*24*60*60)
                return res
            return HttpResponse('ok')
        else:
            return HttpResponse('用户名或密码错误')


def my_default(u):
    if isinstance(u,TUser):
        return {'id':u.id,'name':u.name,'password':u.password}


def register_logic(request):
    user = list(TUser.objects.all())
    return JsonResponse(user,safe=False,json_dumps_params={'default':my_default})


def register(request):
    w = request.GET.get('w',5)
    id = request.GET.get('id')
    level = request.GET.get('level')
    num = request.GET.get('num')
    return render(request,'register.html',{'w':w,'level':level,'id':id,'num':num})


def getcaptcha(request):
    code = random.sample(string.ascii_letters+string.digits,4)
    random_code = "".join(code)
    print(random_code)
    request.session['code']=random_code
    image = ImageCaptcha()
    data = image.generate(random_code)
    return HttpResponse(data,"image/png")


def checkcaptcha(request):
    code = request.session.get('code')
    return HttpResponse(code)


def register_ok1(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    reg = request.POST.get('reg')
    with transaction.atomic():
        if reg == 'flase':
            return HttpResponse('输入信息不全或错误')
        else:
            TUser.objects.create(name=username, password=password)
            request.session['is_login'] = username
            return HttpResponse('OK')

def register_ok(request):
    name = request.GET.get('name')
    w = request.GET.get('w')
    id = request.GET.get('id')
    level = request.GET.get('level')
    num = request.GET.get('num')
    if '@' in name:
        username = '邮箱'
    else:
        username = '手机号码'
    return render(request, 'register ok.html',{'name':name,'username':username,'w':w,'level':level,'id':id,'number':num})

