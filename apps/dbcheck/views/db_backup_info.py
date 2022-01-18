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
    return render(request, 'dbcheck/db_backup_info.html')

def db_backup_info(request):
    page = int(request.POST.get('page', 0))
    limit = int(request.POST.get('limit', 0))
    ip_str = request.POST.get('ipStr', '')
    time_str = request.POST.get('timeStr', '')
    if ip_str == '' and time_str == '':
        sql = """
            SELECT a.ip,a.START_TIME,to_char(a.END_TIME,'yyyy-mm-dd hh24:mi:ss'),a.STATUS 
            FROM backup_status a,server_order b 
            WHERE  a.ip=b.ip and a.gettime>sysdate-30
        """
    else:
        time_str = '0' if time_str == "" else time_str
        sql = """
            SELECT a.ip,a.START_TIME,to_char(a.END_TIME,'yyyy-mm-dd hh24:mi:ss'),a.STATUS 
            FROM backup_status a,server_order b 
            WHERE  a.ip=b.ip and a.gettime>sysdate-%s 
            and to_char(start_time,'YYYY-MM-DD HH24:MI:SS')>= to_char(sysdate-%s,'YYYY-MM-DD HH24:MI:SS') 
            and a.ip like '%s%s%s'
        """ % (time_str,time_str,'%',ip_str,'%')
    objs = oraclehelper.get_db_data_dict(sql=sql,user=user,pwd=pwd,host=host,port=port,sid=sid,keys=['IP','START_TIME','END_TIME','STATUS'])
    objs_one_page = objs['data'][(page - 1) * limit:page * limit]
    res = {'code':0,'count':len(objs['data']),'data':objs_one_page}
    return JsonResponse(res,safe=False,json_dumps_params={'ensure_ascii':False})
