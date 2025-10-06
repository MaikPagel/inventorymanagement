from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_inventory, name='my_inventory'),
    path('signup/',views.signup, name= 'signup'),
    path('edit/', views.edit_inventory, name = 'edit_inventory')
]
