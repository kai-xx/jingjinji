# -*- coding: utf-8 -*
__author__ = 'double k'

import requests
import config
"""
预约
:keyword 预约
"""


class Handle:
    def __init__(self,
                 sessionId,
                 detailInfo,
                 people,
                 date,
                 info):
        self.sessionId = sessionId
        self.subscribeId = info['id']
        self.subscribeCalendarId = date['bookId']
        self.manInfo = detailInfo['man']
        self.people = people
        self.date = date
        self.info = info

    def book(self):
        print("开始执行预约操作")
        data = {
            'subscribeId': self.subscribeId,
            'subscribeCalendarId': self.subscribeCalendarId,
        }
        for man in self.manInfo:
            if man['name'] not in self.people: continue
            data['cardNo_' + man['number']] = man['cardNo']
            data['cardType_' + man['number']] = man['cardType']
            data['userIdCard_' + man['number']] = man['userIdCard']
            data['cardId'] = man['cardId']
        headers = {
            # 'Host': 'zglynk.com',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-cn',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Origin': 'http://zglynk.com',
            # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN',
            # 'Upgrade-Insecure-Requests': '1',
            # 'Referer': 'http://zglynk.com/ITS/itsApp/goSubscribe.action?subscribeId=' + self.subscribeId,
            # 'Content-Length': str(len(dataString)),
            'Cookie': 'JSESSIONID=' + self.sessionId,
            # 'Connection': 'keep-alive'
        }
        response = requests.post('http://zglynk.com/ITS/itsApp/saveUserSubscribeInfo.action',
                                 data=data,
                                 headers=headers)
        print("结束执行预约操作，处理返回值")
        if response.status_code != 200:
            print("请求失败")
            return False
        responseData = response.json()
        print("预约接口返回数据为：", responseData)
        if responseData['status'] in ['1', '4']:
            print(responseData['message'])
            # 如果bookStatus为True时，推送消息到微信
            if config.SERVER_CHAN_CONF['is_server_chan'] == True:
                text = self.info['title'] + " | " + self.date['date'] + " | " + responseData['message']
                requests.get(
                    'https://sc.ftqq.com/'+ config.SERVER_CHAN_CONF['secret'] +'.send?text=' + text)

            return True
        else:
            print(responseData['message'])
            return False
