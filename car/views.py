from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render,redirect
from index.models import TCar,TBook,TUser
# Create your views here.


def car(request):
    w = request.GET.get('w')
    name = request.session.get('is_login')
    if request.COOKIES.get('name'):
        name = request.COOKIES.get('name')
    car = request.session.get('car')
    if name:  #  登录状态
        with transaction.atomic():
            user = TUser.objects.get(name=name)
            user_id = user.id
            if car:
                for i in car.car_list:
                    book_id = i.id
                    count = i.count
                    a = TCar.objects.filter(user_id=user_id,book_id=book_id)
                    if a:
                        a[0].count += int(count)
                        a[0].save()
                    else:
                        TCar.objects.create(user_id=user_id,book_id=book_id,count=count)
                del request.session['car']
            car = Car1(user_id).book(user_id)
            request.session['sum'] = car.sum()
            if w == '4':
                return redirect('order:indent')
    else:        # 未登陆状态
        user_id = 0
    if car:
        kong = 2
    else:
        kong = 1
    return render(request,'car.html',{'name':name,'car':car,'kong':kong,'user':user_id})


def add_car(request):
    id = request.GET.get('id')
    count = request.GET.get('count')
    car = request.session.get('car')
    if count:
        count = int(count)
    else:
        count = 1
    if car:
        car.add_book(id,count)
        request.session['car'] = car
    else:
        car = Car()
        car.add_book(id,count)
        request.session['car']=car
    return HttpResponse('添加成功')

def delete_car(request):
    id = request.GET.get('id')
    car = request.session.get('car')
    car.remove_book(id)
    request.session['car'] = car
    return HttpResponse('删除成功')

def update_car(request):
    id = request.GET.get('id')
    count = request.GET.get('count')
    car = request.session.get('car')
    car.update_book(id=id,count=count)
    request.session['car'] = car
    return HttpResponse('修改成功')

def is_update_car(request):
    name = request.GET.get('name')
    book_id = request.GET.get('id')
    count = request.GET.get('count')
    with transaction.atomic():
        user = TUser.objects.get(name=name)
        user_id = user.id
        use = TCar.objects.get(user_id=user_id,book_id=book_id)
        use.count = int(count)
        use.save()
    return HttpResponse('修改成功')

def is_delete_car(request):
    name = request.GET.get('name')
    book_id = request.GET.get('id')
    user_id = TUser.objects.get(name=name).id
    book = TCar.objects.get(user_id=user_id,book_id=book_id)
    book.delete()
    return HttpResponse('删除成功')

def is_add_car(request):
    name = request.GET.get('name')
    book_id = request.GET.get('id')
    count = request.GET.get('count')
    with transaction.atomic():
        user = TUser.objects.get(name=name)
        user_id = user.id
        use = TCar.objects.filter(user_id=user_id,book_id=book_id)
        if use:
            use[0].count += int(count)
            use[0].save()
        else:
            TCar.objects.create(book_id=book_id,user_id=user_id,count=count)
    return HttpResponse('添加成功')


class Book1:
    def __init__(self,user_id,book_id):
        book = TCar.objects.get(user_id=user_id,book_id=book_id)
        self.id = book_id
        self.count = book.count
        self.title = book.book.title
        self.picture = book.book.picture
        self.price = book.book.dang_price



class Car1:
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
            sum += book.price*int(book.count)
        return round(sum,2)




class Book:
    def __init__(self,id,count):
        book = TBook.objects.get(id=id)
        self.id = id
        self.count = count
        self.title = book.title
        self.picture = book.picture
        self.price = book.dang_price



class Car:
    def __init__(self):
        self.car_list = []
        self.name = 2


    def add_book(self,id,count=1):  # 向购物车添加书籍
        book = self.get_book(id)
        if book:
            book.count += count
        else:
            book = Book(id,count)
            self.car_list.append(book)

    def get_book(self,id):
        for book in self.car_list:
            if book.id == id:
                return book

    def update_book(self,id,count):
        book = self.get_book(id)
        book.count = count

    def remove_book(self,id):
        book = self.get_book(id)
        self.car_list.remove(book)

    def sum(self):
        sum = 0
        for book in self.car_list:
            sum += book.price*int(book.count)
        return round(sum,2)










