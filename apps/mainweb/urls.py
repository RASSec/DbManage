from django.urls import path
from mainweb import views as main_views

urlpatterns = [
    path('',main_views.index,name='main')
]
