from django.shortcuts import render
from utils import oraclehelper
from django.http import JsonResponse

# Create your views here.
user = 'mon_ccc'
pwd = 'Lenovo,2018'
host = '10.114.130.2'
port = '1521'
sid = 'monitor'

def index(request):
    return render(request, 'dbcheck/object_update.html')

def object_update(request):
    page = int(request.POST.get('page', 0))
    limit = int(request.POST.get('limit', 0))
    ip_str = request.POST.get('ipStr', '')
    time_str = request.POST.get('timeStr', '')
    if ip_str == '' and time_str == '':
        sql = """
            select a.ip,a.count_tab,a.gettime from count_tab a,server_order b where a.ip=b.ip and a.gettime>=sysdate-180
        """
    else:
        time_str = '0' if time_str == "" else time_str
        sql = """
        select a.ip,a.count_tab,a.gettime from count_tab a,server_order b where a.ip=b.ip and a.ip like '%s%s%s' and a.gettime>=sysdate-%s
        """ % ('%',ip_str,'%',time_str)
    objs = oraclehelper.get_db_data_dict(sql=sql,user=user,pwd=pwd,host=host,port=port,sid=sid,keys=['IP','COUNT_TAB','GETTIME'])
    objs_one_page = objs['data'][(page - 1) * limit:page * limit]
    res = {'code':0,'count':len(objs['data']),'data':objs_one_page}
    return JsonResponse(res,safe=False,json_dumps_params={'ensure_ascii':False})
