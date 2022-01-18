from django.shortcuts import render,HttpResponse
from utils.oswatch import gen_sqlserver_img
from utils.Helper import ops_renderJSON

# Create your views here.
def index(request):
    return render(request,'sqlservercheck/sqlservercheck.html')

def sqlserver_check_result(request):
    gen_sqlserver_img()
    result = ops_renderJSON(msg='操作成功！')
    return HttpResponse(result)

