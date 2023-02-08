from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('feature',views.feature,name='feature'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login')    
    
]