from django.urls import path
from dbtool.views import dbinstall as dbinstall_views
from dbtool.views import dboper as dboper_views
from dbtool.views import dailycheck as dailycheck_views

urlpatterns = [
    path('dbinstall/',dbinstall_views.index,name='dbinstall'),
    path('dbinstall/dbinstall_result/',dbinstall_views.dbinstall,name='dbinstall_result'),
    path('dboper/',dboper_views.index,name='dboper'),
    path('dboper/dboper_result/',dboper_views.dboper,name='dboper_result'),
    path('dailycheck/',dailycheck_views.index,name='dailycheck'),
    path('dailycheck/dailycheck_result/',dailycheck_views.dailycheck,name='dailycheck_result'),
]
