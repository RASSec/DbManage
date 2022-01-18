from django.urls import path
from dailyoper.views import oswatch as oswatch_views
from dailyoper.views import tbs as tbs_views
from dailyoper.views import aas as aas_views
from dailyoper.views import logoper as logoper_views

urlpatterns = [
    path('oswatch/',oswatch_views.index,name='oswatch'),
    path('oswatch/oswatch_result/',oswatch_views.oswatch,name='oswatch_result'),
    path('tbs/', tbs_views.index, name='tbs'),
    path('tbs/tbs_result/',tbs_views.tbs,name='tbs_result'),
    path('aas/', aas_views.index, name='aas'),
    path('aas/aas_result/',aas_views.aas,name='aas_result'),
    path('logoper/', logoper_views.index, name='logoper'),
    path('logoper/logoper_result/',logoper_views.logoper,name='logoper_result'),
]
