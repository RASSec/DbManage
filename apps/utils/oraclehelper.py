import cx_Oracle

def conn_db(user,pwd,host,port,sid):
    res = {}
    try:
        tns_name = cx_Oracle.makedsn(host=host,port=port,sid=sid)
        conn = cx_Oracle.connect(user, pwd, tns_name)
        res['status'] = True
        res['conn'] = conn
    except Exception as e:
        res['status'] = False
        res['error'] = '连接数据库出现异常！具体原因：' + str(e)
    return res

def get_db_data(sql: str,user,pwd,host,port,sid):
    """
    根据提供的SQL语句，连接数据库查询，返回查询后的结果
    :param sql: 提供的SQL语句
    :return: 返回的数据
    """
    # 获取一个数据库的连接
    rec = conn_db(user,pwd,host,port,sid)
    # 判断是否连接成功
    if not rec['status']:
        return rec
    # 获取一个操作数据库的指针
    cursor = rec['conn'].cursor()
    # 使用异常处理执行语句
    try:
        # 执行获取的传递的SQL语句
        cursor.execute(sql)
        # 获取返回的结果
        rec['data'] = cursor.fetchall()
        # 添加一个错误key
        rec['error'] = ""
    except Exception as e:
        # 修改执行的状态
        rec['status'] = False
        # 添加错误信息
        rec['error'] = '获取数据库数据出现异常！具体原因：' + str(e)
    # 返回
    return rec

def get_db_data_dict(sql, user,pwd,host,port,sid,keys: list):
    """
    获取数据，并转为Dict的格式
    :param sql: 提供的SQL语句
    :param keys: dict的key
    :return: 返回数据的格式 -- [{}，{}，{}，{}，{}，]
    """
    # 调用数据库获取数据
    response = get_db_data(sql,user,pwd,host,port,sid)
    # 判断是否成功
    if not response['status']:
        return response
    # 拼接成字典
    data = []
    # 循环
    for index, value in enumerate(response['data']):
        # 定义一个dict
        temp_dict = {}
        # 遍历
        for i, v in enumerate(value):
            temp_dict[keys[i]] = v
        # 附加到集合
        data.append(temp_dict)
    # 修改携带的数据
    response['data'] = data
    # 返回
    return response


