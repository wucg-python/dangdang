from datetime import datetime,date,time

from django.test import TestCase

# Create your tests here.

def order_no():
    a =b = ''
    for i in str(datetime.now()).split()[1].split(':'):
        a += i
    a = a.split('.')[0]
    for i in str(datetime.now()).split()[0].split('-'):
        b += i
    order_no = (a+b)[:10]
    return order_no

