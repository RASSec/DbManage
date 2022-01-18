from django.shortcuts import render,HttpResponse
from basicweb.models import Major
from django.db.models import Q
from utils.Helper import ops_renderJSON,ops_renderErrJSON
from utils.drawpicture import DataParse

log_path = r"E:\daily_data\log"

def index(request):
    real_db_info = Major.objects.filter(~Q(name="10.114.130.85")).values('name')
    return render(request, 'dailyoper/aas.html', context={'real_db_info': real_db_info})

def aas(request):
    ip4 = request.POST.get('ip4', None)
    time = request.POST.get('time4', None)
    if time is not None:
        time = time.strip('天')
    if ip4 is not None and time is not None:
        DataParse.aas_parse(ip4, time)
        result = ops_renderJSON(msg='AAS报表生成！')
        return HttpResponse(result)
    result = ops_renderErrJSON(msg='请把选项都选全！')
    return HttpResponse(result)
