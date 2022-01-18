from django.shortcuts import render,HttpResponse
from basicweb.models import Major
from django.db.models import Q
from utils.Helper import ops_renderJSON,ops_renderErrJSON
from utils.log import DownLoad,Checklog

log_path = r"E:\daily_data\log"

def index(request):
    username = request.GET.get('username', None)
    real_db_info = Major.objects.filter(~Q(name="10.114.130.85"))
    return render(request, 'dailyoper/logoper.html', context={'username': username, 'real_db_info': real_db_info})

def logoper(request):
    ip2 = request.POST.get('ip2', None)
    btn_name2 = request.POST.get('btn_name2')
    if ip2 is not None:
        if btn_name2 == 'btn_name_2':
            obj = DownLoad('oracle', 'oracle', '10.114.130.2')
            name = obj.get_all_remote_log_filename(ip2, 'alter')
            obj.get_all_remote_log_file(name)
            result = ops_renderJSON(msg='alert日志下载成功！')
            return HttpResponse(result)
        if btn_name2 == 'btn_name_3':
            alterlog_list, _ = Checklog.logclassify(log_path)
            content_list = Checklog.dberror(alterlog_list, ip2)
            result = ops_renderJSON(msg='alert日志查看成功！', data=content_list)
            return HttpResponse(result)
        if btn_name2 == 'btn_name_4':
            obj = DownLoad('oracle', 'oracle', '10.114.130.2')
            name = obj.get_all_remote_log_filename(ip2, 'oslog')
            obj.get_all_remote_log_file(name)
            result = ops_renderJSON(msg='os日志下载成功！')
            return HttpResponse(result)
        if btn_name2 == 'btn_name_5':
            _, oslog_list = Checklog.logclassify(log_path)
            content_list = Checklog.oserror(oslog_list, ip2)
            result = ops_renderJSON(msg='os日志查看成功！', data=content_list)
            return HttpResponse(result)
    result = ops_renderErrJSON(msg='请选择IP地址！')
    return HttpResponse(result)