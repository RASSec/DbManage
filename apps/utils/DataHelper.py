# -*- coding: utf-8 -*-
# @Time     : 2021-09-15 16:00
# @Author   : 胡晓丹
# @FileName : DataHelper.py
# @Software : PyCharm
# @email    : huxd8@lenovo.com

import  datetime
def getCurrentTime( frm = "%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.now()
    return dt.strftime( frm )