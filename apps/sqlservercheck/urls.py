from django.urls import path
from sqlservercheck import views as sqlservercheck_views

urlpatterns = [
    path('',sqlservercheck_views.index,name='sqlservercheck'),
    path('sqlserver_check_result/',sqlservercheck_views.sqlserver_check_result,name='sqlserver_check_result')
]
