from django.urls import path
from login import views as login_views

urlpatterns = [
    path('',login_views.index,name='index'),
    path('login/',login_views.login,name='login'),
    path('reg/',login_views.reg,name='reg'),

]
