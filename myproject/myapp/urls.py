from django.urls import path
from . import views

urlpatterns=[
    path('base/',views.base,name='base'),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('ownership/',views.ownership,name="ownership"),
    path('service/',views.service,name="service"),
    
]