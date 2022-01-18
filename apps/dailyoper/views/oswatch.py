from django.shortcuts import render,HttpResponse
from basicweb.models import Major
from django.db.models import Q
from utils.oswatch import create_all_osw_zip_file,get_remote_osw_zip_file,unzip_local_osw_file,gen_osw_img
from utils.Helper import ops_renderJSON,ops_renderErrJSON

# Create your views here.
def index(request):
    real_db_info = Major.objects.filter(~Q(name="10.114.130.85")).values('name')
    return render(request, 'dailyoper/oswatch.html', context={'real_db_info': real_db_info})

def oswatch(request):
    ip1 = request.POST.get('ip',None)
    btn_name = request.POST.get('btn_name')
    if ip1 is not None:
        if btn_name == 'btn_name_1':
            out_name = create_all_osw_zip_file(username='oracle', password='oracle', hostname='10.114.130.2',ip=ip1)
            get_remote_osw_zip_file(host_ip='10.114.130.2', username='oracle', password='oracle', out_name=out_name,ip=ip1)
            unzip_local_osw_file(ip1)
            result = ops_renderJSON(msg='下载成功！',data=ip1)
            return HttpResponse(result)
        if btn_name == 'btn_name_8':
            gen_osw_img(ip1)
            result = ops_renderJSON(msg='查看成功！',data=ip1)
            return HttpResponse(result)
    result = ops_renderErrJSON(msg='请选择IP地址！')
    return HttpResponse(result)