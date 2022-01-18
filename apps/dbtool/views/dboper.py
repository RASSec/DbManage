from django.shortcuts import render,HttpResponse
from utils.Helper import ops_renderJSON,ops_renderErrJSON
from utils.GetData import get_startuptime_data,get_tbs_used_data,get_update_obj_data,get_scheduler_job_data,get_dbbackup_data,get_archlog_data,get_db_perform_data
from utils.drawpicture import DataParse
from utils.oswatch import gen_sqlserver_img

# Create your views here.
def index(request):
    return render(request, 'dbtool/dboper.html')

# Create your views here.
def dboper(request):
    tag = request.POST.get('tag')
    if tag == '实例启动时间':
        ip = request.POST.get('ip',None)
        tm = request.POST.get('tm',None)
        result = get_startuptime_data(ip.strip(), tm.strip())
        new_result = []
        for index in range(len(result)):
            temp_list = list(result[index])
            new_result.append(temp_list)
        for index in range(len(new_result)):
            new_result[index][-1] = str(new_result[index][-1])
            new_result[index][-2] = str(new_result[index][-2])
        result = ops_renderJSON(data=new_result)
        return HttpResponse(result)
    if tag == '表空间检查':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        result = get_tbs_used_data(ip.strip(), tm.strip())
        new_result = []
        for index in range(len(result)):
            temp_list = list(result[index])
            new_result.append(temp_list)
        for index in range(len(new_result)):
            new_result[index][-1] = str(new_result[index][-1])
        result = ops_renderJSON(data=new_result)
        return HttpResponse(result)
    if tag == '更新对象检查':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        result = get_update_obj_data(ip.strip(), tm.strip())
        new_result = []
        for index in range(len(result)):
            temp_list = list(result[index])
            new_result.append(temp_list)
        for index in range(len(new_result)):
            new_result[index][-1] = str(new_result[index][-1])
        result = ops_renderJSON(data=new_result)
        return HttpResponse(result)
    if tag == '作业调度检查':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        result = get_scheduler_job_data(ip.strip(), tm.strip())
        new_result = []
        for index in range(len(result)):
            temp_list = list(result[index])
            new_result.append(temp_list)
        for index in range(len(new_result)):
            new_result[index][1] = str(new_result[index][1])
            new_result[index][-1] = str(new_result[index][-1])
        result = ops_renderJSON(data=new_result)
        return HttpResponse(result)
    if tag == '备份检查':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        result = get_dbbackup_data(ip.strip(), tm.strip())
        new_result = []
        for index in range(len(result)):
            temp_list = list(result[index])
            new_result.append(temp_list)
        for index in range(len(new_result)):
            new_result[index][1] = str(new_result[index][1])
        result = ops_renderJSON(data=new_result)
        return HttpResponse(result)
    if tag == '归档检查':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        result = get_archlog_data(ip.strip(), tm.strip())
        new_result = []
        for index in range(len(result)):
            temp_list = list(result[index])
            new_result.append(temp_list)
        for index in range(len(new_result)):
            new_result[index][-1] = str(new_result[index][-1])
        result = ops_renderJSON(data=new_result)
        return HttpResponse(result)
    if tag == '性能检查':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        result = get_db_perform_data(ip.strip(), tm.strip())
        new_result = []
        for index in range(len(result)):
            temp_list = list(result[index])
            new_result.append(temp_list)
        for index in range(len(new_result)):
            new_result[index][-1] = str(new_result[index][-1])
        result = ops_renderJSON(data=new_result)
        return HttpResponse(result)
    if tag == '表空间报表':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        tbs = request.POST.get('tbs', None)
        DataParse.tbs_parse(ip, tbs, tm)
        result = ops_renderJSON(msg='表空间报表已生成！')
        return HttpResponse(result)
    if tag == 'aas报表':
        ip = request.POST.get('ip', None)
        tm = request.POST.get('tm', None)
        DataParse.aas_parse(ip, tm)
        result = ops_renderJSON(msg='aas报表已生成！')
        return HttpResponse(result)
    if tag == 'sqlserver巡检':
        gen_sqlserver_img()
        result = ops_renderJSON(msg='sqlserver巡检图片已生成！')
        return HttpResponse(result)
    result = ops_renderErrJSON(msg="操作失败！")
    return HttpResponse(result)
