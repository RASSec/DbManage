# -*- coding: utf-8 -*-
# @Time     : 2021-09-15 16:00
# @Author   : 胡晓丹
# @FileName : UserService.py
# @Software : PyCharm
# @email    : huxd8@lenovo.com

import  random,string,hashlib,base64
class UserService():
    @staticmethod
    def genePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s"%( base64.encodebytes( pwd.encode("utf-8") ),salt)
        m.update( str.encode("utf-8") )
        return m.hexdigest()

    @staticmethod
    def geneSalt( length = 16 ):
       keylist  = [ random.choice( (string.ascii_letters + string.digits ) ) for i in range(length ) ]
       return ( "".join( keylist) )