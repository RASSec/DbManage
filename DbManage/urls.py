"""DbManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 引入include
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 基础数据
    path('basic/',include('basicweb.urls')),
    # 主界面
    path('main/',include('mainweb.urls')),
    # Oracle巡检
    path('dbcheck/', include('dbcheck.urls')),
    # sqlserver巡检
    path('sqlservercheck/',include('sqlservercheck.urls')),
    # 日常操作
    path('dailyoper/', include('dailyoper.urls')),
    # 数据库工具
    path('dbtool/',include('dbtool.urls')),
    # 登录、注册
    path('',include('login.urls'))
]
