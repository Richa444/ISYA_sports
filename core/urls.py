from django.urls import path
from . import views
from .views import donate
from .views import share

urlpatterns = [
    path('testpage', views.test),
    path('home', views.home,name='home'),
    path('header', views.header),
    path('contact/', views.contact,name='contact'),   
    path('show_contact/', views.show_contact,name='show_contact'),
    path('donate/', views.donate, name='donate'),
    path('share/', views.share, name ='share'),
    path('donate1/', views.donate, name=''),

  
]
