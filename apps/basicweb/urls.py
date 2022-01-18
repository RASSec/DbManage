from django.urls import path
from basicweb.views import faculty,major

urlpatterns = [
    # 数据库类型
    path('faculty/',faculty.index,name='faculty'),
    path('faculty/list/',faculty.list_values,name='list_faculty'),
    path('faculty/add/',faculty.add_value,name='add_faculty'),
    path('faculty/edit/',faculty.edit_value,name='edit_faculty'),
    path('faculty/del/',faculty.del_value,name='del_faculty'),

    # 数据库列表
    path('major/',major.index,name='major'),
    path('major/list/',major.list_values,name='list_major'),
    path('major/add/',major.add_value,name='add_major'),
    path('major/edit/',major.edit_value,name='edit_major'),
    path('major/del/',major.del_value,name='del_major')
]