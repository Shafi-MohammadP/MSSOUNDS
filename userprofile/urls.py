from django.urls import path
from . import views

urlpatterns=[

  
    path('',views.userprofile,name='userprofile'),
    path('checkout',views.checkout,name='checkout'),
    
   
]