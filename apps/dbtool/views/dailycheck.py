from django.shortcuts import render,HttpResponse
from utils.Helper import ops_renderJSON,ops_renderErrJSON
from utils.daily import daily
from utils.daily.daily import Checklog
from utils.daily.daily import SendMail
import xlwt
import logging.config
import re

# 配置信息
username = 'mon_ccc'
password = 'Lenovo,2018'
host = '10.114.130.2'
port = '1521'
sid = 'monitor'
xls_name = r"E:\daily_data\数据库日常监控通报-2021-08-08.xls"
new_xls_name = r"E:\daily_data\数据库日常监控通报-2021-08-08_new.xls"
db_info = {'10.114.130.9':'T_130_9','10.114.130.8':'T_130_8','10.114.130.85_R':'T_130_85_REP','10.114.130.85_A':'T_130_85_ARC'}
ip_list = ['10.114.130.198','10.114.130.199','10.114.130.200','10.114.130.201']
arch_dest_1 = "归档路径：\nUSE_DB_RECOVERY_FILE_DEST=+ARCHDG\n"
arch_dest_2 = "归档路径：\n/oracle_data/app/oracle/fast_recovery_area\n"
arch_dest_3 = "归档路径：\n/oracle_data/app/oracle/fast_recovery_area/archivedb\n"
arch_info = {'10.114.130.9':arch_dest_1,'10.114.130.8':arch_dest_1,'10.114.130.85_R':arch_dest_2,'10.114.130.85_A':arch_dest_3}
remote_os_path = "/oratools/sw/oswbb/analysis"
base_dir = r"E:\daily_data"
remote_alertlog_path = "/oracle/home/alterlog"
osw_sheet_list = ['OSW-10.114.130.200','OSW-10.114.130.201','OSW-10.114.130.198','OSW-10.114.130.199']
dblog_sheet_list = ['Alterlog-10.114.130.200','Alterlog-10.114.130.201','Alterlog-10.114.130.198','Alterlog-10.114.130.199']
oslog_sheet_list = ['OSlog-10.114.130.200','OSlog-10.114.130.201','OSlog-10.114.130.198','OSlog-10.114.130.199']
LOG_PATH = r'E:\daily_data\alertlog'

# 日志配置
logging.config.fileConfig('E:\\project\\dbmanage_v4\\common\\libs\\daily\\logger.conf')
logger = logging.getLogger('logger1')

# 配置正则表达式
p_alert = r'alter_(?:\d)*\.log'
p_oslog = r'oslog_(?:\d)*\.log'
p_db_error = r'.*(TNS-)|(ORA-)|(ERROR)|(Error)|(error).*'
p_os_error = r'.*(Error)|(error)|(ERROR)|(WARNING)|(warning)|(Warning).*'
regex_alert = re.compile(p_alert)
regex_oslog = re.compile(p_oslog)
regex_db_error = re.compile(p_db_error)
regex_os_error = re.compile(p_os_error)

# 邮箱配置
mail_host = 'smtp.163.com'
mail_user = '18627947435'
mail_pass = 'DLWCAMWHOLTZLPKA'
sender = '18627947435@163.com'
receivers = ['huxd8@lenovo.com','panly2@lenovo.com']

#excel表格设置写入字体
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = "Microsoft YaHei UI"
font.bold = False        #是否加粗
font.underline = False   #是否有下划线
font.italic = False      #是否为斜体
font.height = 20*9       #字体高度
font.escapement = xlwt.Font.ESCAPEMENT_NONE     #无字体效果
style.font = font

#excel表格设置写入对齐
aligment = xlwt.Alignment()
aligment.vert = xlwt.Alignment.VERT_CENTER       #水平方向向上对齐
aligment.horz = xlwt.Alignment.HORZ_CENTER       #垂直方向向右对齐
style.alignment = aligment

#excel表格设置边框
borders = xlwt.Borders()
borders.top = 1                 #上边框粗细
borders.bottom = 1              #下边框粗细
borders.left = 1                #左边框粗细
borders.right = 1               #右边框粗细
style.borders = borders

#命令
sql_1 = "select distinct(a.startup_time) from table_startup a,server_order b \
where a.gettime>=sysdate-1/24 and a.ip=b.ip and a.ip='%s'"

sql_2 = "select distinct a.tablespace_name,a.used_ratio from tablespace_size_new a,server_order b where a.gettime>=sysdate-1/24 \
and a.ip=b.ip and a.tablespace_name not in ('                TEMP','               TEMP1') \
and a.ip='%s'"

sql_3 = "select distinct a.count_tab \
from count_tab a,server_order b \
where a.ip=b.ip and a.ip='%s' and a.gettime>=sysdate-1/24"

sql_4 = "select distinct distinct a.job_name from mon_scheduler_job a,server_order b \
where a.ip=b.ip and a.ip='%s' and a.gettime>=sysdate-1/24"

sql_5 = "select count(*) from mon_scheduler_job a,server_order b \
where a.ip=b.ip and a.gettime>=sysdate-1/24 \
order by b.id"

sql_6 = "select * from (\
SELECT to_char(a.start_time,'yyyy-mm-dd hh24:mi:ss'),a.STATUS \
FROM new_backup_status a,server_order b \
WHERE  a.ip=b.ip and a.gettime>sysdate-10/24 and a.INPUT_TYPE='DB INCR' and a.ip='%s' \
and to_char(start_time,'YYYY-MM-DD HH24:MI:SS')>= to_char(sysdate-1,'YYYY-MM-DD HH24:MI:SS') \
ORDER BY to_char(a.start_time,'YYYY-MM-DD HH24:MI:SS') desc) \
where rownum=1"

sql_7 = "SELECT distinct a.A \
FROM archive_log a,server_order b \
WHERE a.ip=b.ip and a.gettime>sysdate-1/24 \
and a.ip='%s'and A like '最近一次归档%s'"

sql_8 = "select distinct a.hit from hit_table a ,server_order b ,hit_order c \
WHERE  a.ip=b.ip and a.gettime>sysdate-1/24 and a.ip='%s'\
and substr(a.hit,1,7)=substr(c.name,1,7)"

remote_ls_cmd = "ls -ltrh %s" % remote_os_path
remote_tar_cmd = "zip -r %s.zip %s"
local_unzip_cmd = "unzip %s -d %s"

# Create your views here.
def index(request):
    return render(request,'dbtool/dailycheck.html')

# Create your views here.
def dailycheck(request):
        tag = request.POST.get('tag')
        if tag == '1-获取alert和os日志':
            result_list = daily.get_all_remote_alertlog_filename(username='oracle', password='oracle', hostname='10.114.130.2')
            daily.get_all_remote_alertlog_file(host_ip='10.114.130.2', username='oracle', password='oracle',result_list=result_list)
            result = ops_renderJSON(msg='alert和os日志下载完成！')
            return HttpResponse(result)
        if tag == '2.1-远程生成osw文件':
            for i in ip_list:
                daily.gen_osw_file(i)
                logger.info('{0}节点oswatch文件已经生成！'.format(i))
            result = ops_renderJSON(msg='远程已经生成osw文件！')
            return HttpResponse(result)
        if tag == '2.2-远程压缩获取osw文件':
            out_name = daily.create_all_osw_zip_file(username='oracle', password='oracle', hostname='10.114.130.2')
            daily.get_remote_osw_zip_file(host_ip='10.114.130.2', username='oracle', password='oracle', out_name=out_name)
            result = ops_renderJSON(msg='远程压缩获取osw文件成功！')
            return HttpResponse(result)
        if tag == '2.3-本地解压osw文件':
            daily.unzip_local_osw_file(ip_list)
            result = ops_renderJSON(msg='本地解压osw文件成功！')
            return HttpResponse(result)
        if tag == '2.4-生成osw截图':
            daily.gen_osw_img(ip_list)
            result = ops_renderJSON(msg='本地生成osw截图成功！')
            return HttpResponse(result)
        if tag == '3-oracle监控指标获取并写入excel表':
            db_list = list(db_info)
            daily.write_oracle_parameter(db_list)
            result = ops_renderJSON(msg='oracle监控指标获取并写入excel表成功！')
            return HttpResponse(result)
        if tag == '4-osw图片写入到excel表':
            daily.write_osw_img()
            result = ops_renderJSON(msg='osw图片写入到excel表成功！')
            return HttpResponse(result)
        if tag == '5-sqlserver图片写入到excel表':
            daily.write_sqlserver_img()
            result = ops_renderJSON(msg='sqlserver图片写入到excel表成功！')
            return HttpResponse(result)
        if tag == '6-alert日志写入到excel表':
            daily.write_dblog()
            result = ops_renderJSON(msg='alert日志写入到excel表成功！')
            return HttpResponse(result)
        if tag == '7-os日志写入到excel表':
            daily.write_oslog()
            result = ops_renderJSON(msg='os日志写入到excel表成功！')
            return HttpResponse(result)
        if tag == '8-alert日志错误检查':
            alterlog_list, _ = Checklog.logclassify(LOG_PATH)
            resu = Checklog.dberror(alterlog_list)
            msg = ''.join(resu)
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '9-os日志错误检查':
            _, oslog_list = Checklog.logclassify(LOG_PATH)
            resu = Checklog.oserror(oslog_list)
            msg = ''.join(resu)
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '10-发送日报日志':
            mail = SendMail(mail_host, mail_user, mail_pass, sender, receivers)
            mail.sendmail()
            result = ops_renderJSON(msg='发送日报日志成功！')
            return HttpResponse(result)
        result = ops_renderErrJSON(msg="操作失败！")
        return HttpResponse(result)
