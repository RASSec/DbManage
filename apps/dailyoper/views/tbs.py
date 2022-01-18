from django.shortcuts import render,HttpResponse
from basicweb.models import Major
from django.db.models import Q
from utils.Helper import ops_renderJSON,ops_renderErrJSON
from utils.drawpicture import DataParse

log_path = r"E:\daily_data\log"

def index(request):
    real_db_info = Major.objects.filter(~Q(name="10.114.130.85")).values('name')
    return render(request, 'dailyoper/tbs.html', context={'real_db_info': real_db_info})

def tbs(request):
    ip3 = request.POST.get('ip3', None)
    type = request.POST.get('type3', None)
    time = request.POST.get('time3', None)
    if time is not None:
        time = time.strip('天')
    if ip3 is not None and type is not None and time is not None:
        DataParse.tbs_parse(ip3, type, time)
        result = ops_renderJSON(msg='表空间报表生成！')
        return HttpResponse(result)
    return ops_renderErrJSON(msg='表空间报表生成失败！')
