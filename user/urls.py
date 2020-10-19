from django.urls import path
from user import views
app_name = 'user'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('register_ok/',views.register_ok,name='register_ok'),
    path('login_logic/',views.login_logic,name='login_logic'),
    path('register_logic/',views.register_logic,name='register_logic'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('checkcaptcha/',views.checkcaptcha,name='checkcaptcha'),
    path('register_ok1/',views.register_ok1,name='register_ok1'),
    # path('shop/',views.shop,name='shop'),

]