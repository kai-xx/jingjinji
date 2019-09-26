# -*- coding: utf-8 -*
__author__ = 'double k'

import requests
from bs4 import BeautifulSoup
class Detail:
    def __init__(self, sessionId, url):
        self.sessionId = sessionId
        self.url = url
    def getDetail(self):
        print("开始执行获取详情操作")
        headers = {
            # 'Host': 'zglynk.com',
            'Cookie': 'JSESSIONID=' + self.sessionId,
            # 'Upgrade-Insecure-Requests': '1',
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN',
            # 'Referer': 'http://zglynk.com/ITS/itsApp/subscribeList.jsp',
            # 'Accept-Language': 'zh-cn',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Connection': 'keep-alive'
        }
        response = requests.get('http://zglynk.com/ITS/itsApp/' + self.url,
                                headers=headers)
        print("结束执行获取详情操作，处理返回值")
        if response.status_code != 200:
            print("请求失败")
            return False
        return self.handleHtml(response.text)
        # detailHtml = response.text
        # fo = open("detail.html", "w")
        # fo.write(detailHtml)
        # # 关闭打开的文件
        # fo.close()
        # print(detailHtml)
    def handleHtml(self, html):
        soup = BeautifulSoup(html, "lxml")
        detail = {}
        detailInfo = soup.find("div", class_="block marl25 marr25")
        print("---------------------------------------------")
        print(detailInfo.text)

        detail['date'] = self.getBookTime(soup)

        detail['man'] = self.getBookMan(soup)
        print("---------------------------------------------", "\n\n")
        return detail
    def getBookTime(self, soup):
        dateInfos = soup.find("div", class_="mart30").find("table", class_="ticket-info mart20").find_all('tr')
        dates = []
        for dateInfo in dateInfos:
            d = dateInfo.select("td:nth-of-type(1)")
            if len(d) > 0 :
                date = d[0].string
            else:
                continue
            s = dateInfo.select("td:nth-of-type(3)")
            status = "".join(line.strip() for line in s[0].text.split("\n")) if len(s) > 0 else ""
            bookInfo = dateInfo.find(id="subscribeCalendarId")
            bookId = bookInfo['value'] if bookInfo != None else 0
            print("日期：", date, "    ", status, "    预约ID为：", bookId)
            if bookId == 0: continue
            if status != "可预约": continue
            dates.append({
                "date": date,
                "status": status,
                "bookId": bookId
            })
        return dates
    def getBookMan(self, soup):
        manInfos = soup.find("div", class_="mart40").find("table", class_="ticket-info mart20").find_all('tr')
        man = []
        for manInfo in manInfos:
            name = manInfo.find("span", class_="font36").string
            cardId = manInfo.find("input", id="cardId")['value']
            number = cardId.split("#", 2)[0]
            cardNo = manInfo.find("input", id="cardNo_" + number)['value']
            cardType = manInfo.find("input", id="cardType_" + number)['value']
            userIdCard = manInfo.find("input", id="userIdCard_" + number)['value']
            data = {
                "name": name,
                "cardId": cardId,
                "number": number,
                "cardNo": cardNo,
                "cardType": cardType,
                "userIdCard": userIdCard,
            }
            man.append(data)
            print("身份信息为：", data)
        return man

# fo = open("detail.html")
# html = fo.read()
# # 关闭打开的文件
# fo.close()
# sessionId =""
# url ="goSubscribe.action?subscribeId=9"
# detail = Detail(sessionId, url)
# # detail.getDetail()
# detail.handleHtml(html)