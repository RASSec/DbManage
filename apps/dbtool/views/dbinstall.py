from django.shortcuts import render,HttpResponse
from utils.Helper import ops_renderJSON,ops_renderErrJSON
from utils.oracle_install import oracle_install
from utils.oracle_install.oper import Oper
import configparser

nr_hugepages = None

# Create your views here.
def index(request):
    return render(request,'dbtool/dbinstall.html')

# Create your views here.
def dbinstall(request):
        global nr_hugepages
        tag = request.POST.get('tag')
        if tag == '1.1-系统版本检查':
            user = request.POST.get('user').strip()
            pwd = request.POST.get('pwd').strip()
            ip = request.POST.get('ip').strip()
            if ip == '' or user == '' or pwd == '':
                result = ops_renderErrJSON(msg='请把输入框填写完整！退出安装！')
                return HttpResponse(result)
            msg = oracle_install.DbInstall.os_release_check(user,pwd,ip)
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '1.2-系统内存检查':
            user = request.POST.get('user').strip()
            pwd = request.POST.get('pwd').strip()
            ip = request.POST.get('ip').strip()
            if ip == '' or user == '' or pwd == '':
                result = ops_renderErrJSON(msg='请把输入框填写完整！退出安装！')
                return HttpResponse(result)
            msg = oracle_install.DbInstall.os_memory_check(user,pwd,ip)
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '1.3-系统swap检查':
            user = request.POST.get('user').strip()
            pwd = request.POST.get('pwd').strip()
            ip = request.POST.get('ip').strip()
            if ip == '' or user == '' or pwd == '':
                result = ops_renderErrJSON(msg='请把输入框填写完整！退出安装！')
                return HttpResponse(result)
            msg = oracle_install.DbInstall.os_swap_check(user,pwd,ip)
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '1.4-安装目录检查':
            user = request.POST.get('user').strip()
            pwd = request.POST.get('pwd').strip()
            ip = request.POST.get('ip').strip()
            if ip == '' or user == '' or pwd == '':
                result = ops_renderErrJSON(msg='请把输入框填写完整！退出安装！')
                return HttpResponse(result)
            msg = oracle_install.DbInstall.oracle_installdir_check(user,pwd,ip)
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '2-安装软件上传':
            user = request.POST.get('user').strip()
            pwd = request.POST.get('pwd').strip()
            ip = request.POST.get('ip').strip()
            if ip == '' or user == '' or pwd == '':
                result = ops_renderErrJSON(msg='请把输入框填写完整！退出安装！')
                return HttpResponse(result)
            dbsoft_base_dir = 'E:\\project\\DbManage\\apps\\utils\\oracle_install\\dbsoft\\'
            remote_soft_dir = '/dbsoft/'
            dbsoft_file = 'LINUX.X64_193000_db_home.zip'
            opatch_file = 'p6880880_190000_Linux-x86-64.zip'
            patch_file = 'p32545013_190000_Linux-x86-64.zip'
            mkdir_cmd = 'mkdir -p {0};echo $?'.format(remote_soft_dir)
            obj = Oper(user, pwd, ip)
            mkdir_result = obj.command(mkdir_cmd)
            if int(mkdir_result.strip('\n').strip()) == 0:
                print('{0}远程服务器创建目录{1}成功！'.format(ip, remote_soft_dir))
                print('{0}正在上传！'.format(dbsoft_file))
                db_local_file = dbsoft_base_dir + dbsoft_file
                db_remote_file = remote_soft_dir + dbsoft_file
                obj.upload(db_local_file, db_remote_file)
                print('{0}上传成功！'.format(dbsoft_file))
                print('{0}正在上传！'.format(opatch_file))
                opatch_local_file = dbsoft_base_dir + opatch_file
                opatch_remote_file = remote_soft_dir + opatch_file
                obj.upload(opatch_local_file, opatch_remote_file)
                print('{0}上传成功！'.format(opatch_file))
                print('{0}正在上传！'.format(patch_file))
                patch_local_file = dbsoft_base_dir + patch_file
                patch_remote_file = remote_soft_dir + patch_file
                obj.upload(patch_local_file, patch_remote_file)
                print('{0}上传成功！'.format(patch_file))
            else:
                print('{0}远程服务器创建目录{1}失败！'.format(ip, remote_soft_dir))
                result = ops_renderErrJSON(msg='远程服务器创建oracle软件目录失败！')
                return HttpResponse(result)
            result = ops_renderJSON(msg='oracle所有安装软件上传成功！')
            return HttpResponse(result)
        if tag == '3-生成安装配置文件':
            ora_ins_dir = request.POST.get('ora_ins_dir').strip()
            ora_tool_dir = request.POST.get('ora_tool_dir').strip()
            ora_data_dir = request.POST.get('ora_data_dir').strip()
            ora_arch_dir = request.POST.get('ora_arch_dir').strip()
            oracle_base = request.POST.get('oracle_base').strip()
            oracle_home = request.POST.get('oracle_home').strip()
            ora_pwd = request.POST.get('ora_pwd').strip()
            ora_sid = request.POST.get('ora_sid').strip()
            client_lang = request.POST.get('client_lang').strip()
            sga_size = request.POST.get('sga_size').strip()
            ip = request.POST.get('ip').strip()
            host = request.POST.get('host').strip()
            soft_dir = request.POST.get('soft_dir').strip()
            root_pwd = request.POST.get('root_pwd').strip()
            db_soft = request.POST.get('db_soft').strip()
            sys_pwd = request.POST.get('sys_pwd').strip()
            system_pwd = request.POST.get('system_pwd').strip()
            db_mem = request.POST.get('db_mem').strip()
            db_lang = request.POST.get('db_lang').strip()
            opatch_file = request.POST.get('opatch_file').strip()
            opatch = request.POST.get('opatch').strip()
            if ora_ins_dir == '' or ora_tool_dir == '' or ora_data_dir == '' or ora_arch_dir == '' or oracle_base == '' or oracle_home == '' \
                or ora_pwd == '' or ora_sid == '' or client_lang == '' or sga_size == '' or ip == '' or host == '' or soft_dir == '' \
                or root_pwd == '' or db_soft == '' or sys_pwd == '' or system_pwd == '' or db_mem == '' or db_lang == '' or opatch_file == '' or opatch == '':
                result = ops_renderErrJSON(msg='请把输入框填写完整！退出安装！')
                return HttpResponse(result)
            oracle_dir = 'oracle_dir = ' + ora_ins_dir + '\n'
            oracle_tool = 'oracle_tool = ' + ora_tool_dir + '\n'
            data_dir = 'data_dir = ' + ora_data_dir + '\n'
            archive_dir = 'archive_dir = ' + ora_arch_dir + '\n'
            oracle_base = 'oracle_base = ' + oracle_base + '\n'
            oracle_home = 'oracle_home = ' + oracle_home + '\n'
            oracle_pwd = 'oracle_pwd = ' + ora_pwd + '\n'
            oracle_sid = 'oracle_sid = ' + ora_sid + '\n'
            nls_lang = 'nls_lang = ' + client_lang + '\n'
            sga_size = 'sga_size = ' + sga_size + '\n'
            ip = 'ip = ' + ip + '\n'
            hostname = 'hostname = ' + host + '\n'
            dbsoft_dir = 'dbsoft_dir = ' + soft_dir + '\n'
            root_pwd = 'root_pwd = ' + root_pwd + '\n'
            db_zip_file = 'db_zip_file = ' + db_soft + '\n'
            sys_pwd = 'sys_pwd = ' + sys_pwd + '\n'
            system_pwd = 'system_pwd = ' + system_pwd + '\n'
            db_total_mem = 'db_total_mem = ' + db_mem + '\n'
            lang = 'lang = ' + db_lang + '\n'
            opatch_name = 'opatch_name = ' + opatch_file + '\n'
            patch_name = 'patch_name = ' + opatch + '\n'
            config_list = []
            config_list.append('[pre_oracle_oinstall]\n')
            config_list.append(oracle_dir)
            config_list.append(oracle_tool)
            config_list.append(data_dir)
            config_list.append(archive_dir)
            config_list.append(oracle_base)
            config_list.append(oracle_home)
            config_list.append(oracle_pwd)
            config_list.append(oracle_sid)
            config_list.append(nls_lang)
            config_list.append(sga_size)
            config_list.append(ip)
            config_list.append(hostname)
            config_list.append('\n')
            config_list.append('[db_install]\n')
            config_list.append(dbsoft_dir)
            config_list.append(root_pwd)
            config_list.append(db_zip_file)
            config_list.append(sys_pwd)
            config_list.append(system_pwd)
            config_list.append(db_total_mem)
            config_list.append(lang)
            config_list.append('\n')
            config_list.append('[patch_install]\n')
            config_list.append(opatch_name)
            config_list.append(patch_name)
            base_dir = 'E:\\project\\DbManage\\apps\\utils\\oracle_install\\'
            config_file = base_dir + 'setup.conf'
            try:
                with open(file=config_file, mode='w', encoding='utf-8') as f:
                    f.writelines(config_list)
            except Exception as e:
                print('配置文件写入失败！')
                print('错误信息：{0}'.format(e))
                result = ops_renderErrJSON(msg='数据库安装配置文件生成失败！')
                return HttpResponse(result)
            result = ops_renderJSON(msg='数据库安装配置文件已经生成！')
            return HttpResponse(result)
        if tag == '4.1-禁用防火墙':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.stop_firewall('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '4.2-禁用selinux':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.stop_selinux('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '5-rpm包安装':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.rpm_install('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '6.1-创建用户和组':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.user_group_add('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '6.2-创建目录':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.create_dir('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '7.1-bash_profile配置':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.modify_oracle_profile('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '7.2-sysctl.conf配置':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg,nr_hugepages = oracle_install.DbInstall.modify_os_parameter_1('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '7.3-limits.conf配置':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.modify_os_parameter_2('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '7.4-profile配置':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.modify_profile('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '7.5-hosts配置':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.modify_host('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '8-关闭透明大页':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            msg = oracle_install.DbInstall.stop_transparent_hugepage('root', sec2['root_pwd'], sec1['ip'],nr_hugepages)
            result = ops_renderJSON(msg=msg)
            return HttpResponse(result)
        if tag == '9-数据库软件安装':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            oracle_install.DbInstall.unzip_db_file('root', sec2['root_pwd'], sec1['ip'])
            install_result = oracle_install.DbInstall.db_software_install('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=install_result)
            return HttpResponse(result)
        if tag == '10-数据库监听安装':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            install_result = oracle_install.DbInstall.listener_install('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=install_result)
            return HttpResponse(result)
        if tag == '11-数据库安装':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            install_result = oracle_install.DbInstall.db_install('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=install_result)
            return HttpResponse(result)
        if tag == '12-补丁安装':
            config = configparser.ConfigParser()
            config.read('E:\\project\\DbManage\\apps\\utils\\oracle_install\\setup.conf', encoding='utf-8')
            sec1 = config['pre_oracle_oinstall']
            sec2 = config['db_install']
            install_result = oracle_install.DbInstall.patch_install('root', sec2['root_pwd'], sec1['ip'])
            result = ops_renderJSON(msg=install_result)
            return HttpResponse(result)
        result = ops_renderErrJSON(msg="操作失败！")
        return HttpResponse(result)


