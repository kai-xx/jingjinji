# -*- coding: utf-8 -*
__author__ = 'double k'

import requests

"""
登录
:keyword login
"""


class Login:
    def __init__(self, phone, password, sessionId):
        self.url = "http://zglynk.com/ITS/itsApp/login.action"
        self.phone = phone
        self.password = password
        self.sessionId = sessionId

    def login(self):
        print("开始执行登录操作")
        # dataString = "userPhone=" + self.phone +"&loginPassword=" + self.password
        data = {
            "userPhone": self.phone,
            "loginPassword": self.password
        }
        headers = {
            # 'Host': 'zglynk.com',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-cn',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Origin': 'http://zglynk.com',
            # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN',
            # 'Upgrade-Insecure-Requests': '1',
            # 'Referer': 'http://zglynk.com/ITS/itsApp/login.jsp',
            # 'Content-Length': str(len(dataString)),
            'Cookie': 'JSESSIONID=' + self.sessionId,
        }
        response = requests.post('http://zglynk.com/ITS/itsApp/login.action',
                                 data=data,
                                 headers=headers)
        print("结束执行登录操作，处理返回值")
        if response.status_code != 200:
            print("请求失败")
            return False
        responseData = response.json()
        print("登录接口返回数据为：", responseData)
        if responseData['status'] == '1':
            print(responseData['message'])
            return True
        else:
            print(responseData['message'])
            return False
