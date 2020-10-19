from django.db import transaction
from django.shortcuts import render
from index.models import TCar,TBook,TUser,TAddress,TOrder,TOrderItem
from django.http import JsonResponse, HttpResponse
from datetime import datetime,date

# Create your views here.
def indent(request):
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')
    user = TUser.objects.get(name=name)
    user_id = user.id
    books = Order(user_id).book(user_id)
    addresses = TAddress.objects.filter(user_id=user_id)
    return render(request,'indent.html',{'books':books,'addresses':addresses,'name':name})


def address(request):
    detail = request.POST.get('detail')
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')
    user = TUser.objects.get(name=name)
    user_id = user.id
    ars = TAddress.objects.get(address=detail,user_id=user_id)
    return JsonResponse(ars,safe=False,json_dumps_params={'default':my_default})

def submit(request):
    detail = request.POST.get('detail')
    client = request.POST.get('client')
    post_code = request.POST.get('post_code')
    cellphone = request.POST.get('cellphone')
    telephone = request.POST.get('telephone')
    request.session['address'] = detail
    request.session['username'] = client
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')
    user = TUser.objects.get(name=name)
    user_id = user.id
    if TAddress.objects.filter(user_id=user_id,address=detail):
        pass
    else:
        if telephone == '':
            TAddress.objects.create(user_id=user_id,address=detail,name=client,post_code=post_code,cellphone=cellphone)
        elif cellphone == '':
            TAddress.objects.create(user_id=user_id, address=detail, name=client, post_code=post_code,telephone=telephone)
        else:
            TAddress.objects.create(user_id=user_id, address=detail, name=client, post_code=post_code,cellphone=cellphone,telephone=telephone)
    return HttpResponse('OK')


def my_default(u):
    if isinstance(u,TAddress):
        return {'address':u.address,'cellphone':u.cellphone,'post_code':u.post_code,'name':u.name,'tellphone':u.tellphone}



def indent_ok(request):
    address = request.session.get('address')
    username = request.session.get('username')
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')
    user = TUser.objects.get(name=name)
    user_id = user.id
    books = Order(user_id).book(user_id)
    order_id = books.order_no()
    create_time = datetime.now()
    total = books.total()
    with transaction.atomic():
        TOrder.objects.create(order_id=order_id,create_time=create_time,total=total,user_id=user_id,address=address)
        order = TOrder.objects.get(user_id=user_id,order_id=order_id)
        id = order.id
        for book in books.car_list:
            TOrderItem.objects.create(order_id=id,book_id=book.id,count=book.count)
        TCar.objects.filter(user_id=user_id).delete()
    return render(request,'indent ok.html',{'name':name,'order_id':order_id,'total':total,'username':username,'sum':books.sum()})




class Book1:
    def __init__(self,user_id,book_id):
        book = TCar.objects.get(user_id=user_id,book_id=book_id)
        self.id = book_id
        self.count = book.count
        self.title = book.book.title
        self.dang_price = book.book.dang_price
        self.price = book.book.price

    def disc(self):
        disc = round(self.dang_price/self.price*10,2)
        return disc

    def total(self):
        total = round(self.dang_price*self.count,2)
        return total



class Order:
    def __init__(self,user_id):
        self.books = TCar.objects.filter(user_id=user_id)
        self.car_list = []
        self.name = 2

    def book(self,user_id):
        for i in self.books:
            book = Book1(user_id,i.book_id)
            self.car_list.append(book)
        return self

    def sum(self):
        sum = 0
        for book in self.car_list:
            sum += book.dang_price*int(book.count)
        return round(sum,2)

    def total(self):
        total = 0
        for book in self.car_list:
            total += book.count
        return total

    def order_no(self):
        a = b = ''
        for i in str(datetime.now()).split()[1].split(':'):
            a += i
        a = a.split('.')[0]
        for i in str(datetime.now()).split()[0].split('-'):
            b += i
        order_no = int((a + b)[:10])
        return order_no
