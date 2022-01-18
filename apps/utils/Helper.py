# -*- coding: utf-8 -*-
# @Time     : 2021-09-15 16:00
# @Author   : 胡晓丹
# @FileName : Helper.py
# @Software : PyCharm
# @email    : huxd8@lenovo.com

import json

def ops_renderJSON( code = 200,msg = "操作成功~~",data = {} ):
    resp = { "code":code,"msg":msg,"data":data }
    result = json.dumps(resp, ensure_ascii=False)
    return result

def ops_renderErrJSON( msg = "系统繁忙，请稍后再试~~",data = {} ):
    return ops_renderJSON( code = -1,msg = msg,data = data )
