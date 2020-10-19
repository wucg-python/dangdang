from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect
from index.models import TCategory, TBook, TUser


# Create your views here.

def index(request):
    cates1 = TCategory.objects.filter(level=1)
    cates2 = TCategory.objects.filter(level=2)
    books = TBook.objects.order_by('-launch_time')[:8]
    books1 = TBook.objects.order_by('-launch_time')[:6]
    books1 = sorted(books1,key=lambda item:item.sales_nummber,reverse=True)
    books2 = books1[:3]
    books3 = books1[3:6]
    books4 = TBook.objects.all().order_by('-comment_nummber')[:8]
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')

    return render(request,'index.html',{'cates1':cates1,'cates2':cates2,'books':books,'books2':books2,'books3':books3,'books4':books4,'name':name})


def booklist(request):
    cates1 = TCategory.objects.filter(level=1)
    cates2 = TCategory.objects.filter(level=2)
    level = request.GET.get('level')
    id = int(request.GET.get('id'))
    if level == '1':
        books = TBook.objects.filter(cates__parent_id=id)
    elif level == '2':
        books = TBook.objects.filter(cates_id=id)
    else:
        books = TBook.objects.all()
    # 分页
    num = request.GET.get('num', 1)
    pagtor = Paginator(books,per_page=4)
    page = pagtor.page(num)
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')

    return render(request,'booklist.html',{'cates1':cates1,'cates2':cates2,'page':page,'level':level,'id':id,'name':name})


def book_details(request):
    id = request.GET.get('id')
    print(id)
    book = TBook.objects.get(id=id)
    cates1 = TCategory.objects.filter(level=1)
    discount = round(book.dang_price/book.price*10,2)
    parent_id = int(book.cates.parent_id)
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')
    if name:
        user = TUser.objects.get(name=name)
        user_id = user.id
    else:
        user_id = 0
    return render(request,'Book details.html',{'book':book,'discount':discount,'cates1':cates1,'parent_id':parent_id,'name':name,'id':id,'user':user_id})


def exit(request):
    request.session.clear()
    response = HttpResponse('退出成功')
    response.set_cookie('name',123,max_age=0)
    return response

