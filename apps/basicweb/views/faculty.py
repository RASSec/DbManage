# 引入模块
from django.shortcuts import render
# 引入数据库通用类
from utils import sqlhelper
# 引入JsonResponse
from django.http import JsonResponse
# 导入类
from basicweb.models import Faculty

def index(request):
    return render(request,'basic/faculty.html')

def list_values(request):
    """获取院系的数据"""
    # 接收查询的条件
    q_str = request.POST.get('queryStr',"")
    # 准备SQL语句
    sql = """
    select t3.id,t3.name,count(t3.id2) as 'Number'
    from 
    (
    select t1.id,t1.name,t2.id as 'id2'
    from Basic_Faculty as t1
    left join Basic_Major as t2
    on t1.id=t2.faculty_id where t1.name like '%s'
    ) as t3
    group by t3.id,t3.name;
    """ % ('%' + q_str + '%')
    # 开始执行
    response = sqlhelper.get_db_data_dict(sql,['id','name','number'])
    # 判断
    if response['status']:
        return JsonResponse({'status':True,'data':response['data']})
    else:
        return JsonResponse({'status':False,'error': response['error']})

def add_value(request):
    """添加"""
    # 接收传递过来的名称
    name = request.POST.get('name')
    try:
        # 写入数据库
        Faculty.objects.create(name=name)
        return JsonResponse({'status':True})
    except Exception as e:
        return JsonResponse({'status':False,'error':'写入数据库出现异常，具体原因：' + str(e)})

def edit_value(request):
    """修改"""
    # 获取传递过来的数据
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    # 修改
    try:
        obj = Faculty.objects.get(id=id)
        obj.name = name
        obj.save()
        return JsonResponse({'status':True})
    except Exception as e:
        return JsonResponse({'status':False,'error':'修改提交到数据库出现异常，具体原因：' + str(e)})

def del_value(request):
    """删除"""
    # 获取id
    id = request.POST.get('id')
    # 删除
    try:
        Faculty.objects.get(id=id).delete()
        return JsonResponse({'status':True})
    except Exception as e:
        return JsonResponse({'status':False,'error':'删除提交到数据库出现异常，具体原因：' + str(e)})
