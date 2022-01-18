from django.urls import path
from dbcheck.views import startup_time as startup_time_views
from dbcheck.views import tbs_used as tbs_used_views
from dbcheck.views import object_update as object_update_views
from dbcheck.views import scheduler_job as scheduler_job_views
from dbcheck.views import db_backup_info as db_backup_info_views
from dbcheck.views import db_archive_info as db_archive_info_views
from dbcheck.views import db_performance_info as db_performance_info_views

urlpatterns = [
    path('startup_time/',startup_time_views.index,name='startup_time'),
    path('startup_time/list_value/',startup_time_views.startup_time,name='list_startup_time'),
    path('tbs_used/',tbs_used_views.index,name='tbs_used'),
    path('tbs_used/list_value/',tbs_used_views.tbs_used,name='list_tbs_used'),
    path('object_update/',object_update_views.index,name='object_update'),
    path('object_update/list_value/',object_update_views.object_update,name='list_object_update'),
    path('scheduler_job/',scheduler_job_views.index,name='scheduler_job'),
    path('scheduler_job/list_value/',scheduler_job_views.scheduler_job,name='list_scheduler_job'),
    path('db_backup_info/',db_backup_info_views.index,name='db_backup_info'),
    path('db_backup_info/list_value/',db_backup_info_views.db_backup_info,name='list_db_backup_info'),
    path('db_archive_info/',db_archive_info_views.index,name='db_archive_info'),
    path('db_archive_info/list_value/',db_archive_info_views.db_archive_info,name='list_db_archive_info'),
    path('db_performance_info/',db_performance_info_views.index,name='db_performance_info'),
    path('db_performance_info/list_value/',db_performance_info_views.db_performance_info,name='list_db_performance_info')
]