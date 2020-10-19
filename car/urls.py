from django.urls import path
from car import views
app_name = 'car'

urlpatterns = [
    path('car/',views.car,name='car'),
    path('add_car/',views.add_car,name='add_car'),
    path('delete_car/',views.delete_car,name='delete_car'),
    path('is_add_car/',views.is_add_car,name='is_add_car'),
    path('is_delete_car/',views.is_delete_car,name='is_delete_car'),
    path('update_car/',views.update_car,name='update_car'),
    path('is_update_car/',views.is_update_car,name='is_update_car'),


]