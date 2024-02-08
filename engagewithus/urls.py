from django.urls import path
from . import views

urlpatterns = [
   
    path('volunteer/', views.volunteer, name='volunteer'),
    path('wts/', views.what_they_say),
    path('show_volunteer/', views.show_volunteer, name ='show_volunteer'),
    
    
]
