
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('test',views.home2,name='test'),
    path('test2',views.home3,name='test2'),
    path('calc', views.calculator, name='calc'),
    path('calc2', views.calculatorfun, name='calc2'),
    path('calc3', views.calc3, name='calc3')
]
