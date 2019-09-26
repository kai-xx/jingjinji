# -*- coding: utf-8 -*
__author__ = 'double k'

import requests
from bs4 import BeautifulSoup
class List:
    def __init__(self, sessionId):
        self.sessionId = sessionId

    def getList(self):
        print("开始执行获取列表操作")
        headers = {
            # 'Host': 'zglynk.com',
            'Cookie': 'JSESSIONID=' + self.sessionId,
            # 'Upgrade-Insecure-Requests': '1',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN',
            # 'Referer': 'http://zglynk.com/ITS/itsApp/goIndex.action',
            # 'Accept-Language': 'zh-cn',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Connection': 'keep-alive'
        }
        response = requests.get('http://zglynk.com/ITS/itsApp/subscribeList.jsp',
                                headers=headers)
        print("结束执行获取列表操作，处理返回值")
        if response.status_code != 200:
            print("请求失败")
            return False
        return self.handleHtml(response.text)
        # fo = open("list.html", "w")
        # fo.write(listHtml)
        # # 关闭打开的文件
        # fo.close()
    def handleHtml(self, html):
        soup = BeautifulSoup(html, "lxml")
        listData = [];
        for li in soup.find_all('li'):
            href = li.a['href']
            title = li.a.find('p', class_="font34").string
            content = li.a.find('p', class_="").string
            id = href.split("=", 1)[1]
            data = {
                "url": href,
                "id": id,
                "title": title,
                "content": content
            }
            print("---------------------------------------------")
            print("链接: ", href)
            print("ID: ", id)
            print("标题: ", title)
            print("内容: ", content)
            print("---------------------------------------------", "\n\n")
            listData.append(data)
        return listData

# fo = open("list.html")
# html = fo.read()
# # 关闭打开的文件
# fo.close()
# list = List()
# list.handleHtml(html)