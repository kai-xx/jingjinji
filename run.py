# -*- coding: utf-8 -*
__author__ = 'double k'

import os
import loginClass
import listClass
import detailClass
import handleClass
import time
import config
from threading import Thread

phone = config.USERNAME
password = config.PASSWORD
sessionId = config.SESSION_ID
people = config.PEOPLE
selectData = config.SELECT_DATA

def checkLogin():
    # 获取登录时间
    fo = open("login-time")
    st = fo.read()
    # 关闭打开的文件
    fo.close()
    loginTime = 0 if st == "" else int(st)
    diff = int(time.time()) - loginTime
    return True if diff < 7200 and loginTime > 0 else False

if (checkLogin() == False):
    # 登录操作
    login = loginClass.Login(phone, password, sessionId)
    loginType = login.login()
    if loginType == False:
        print("结束运行")
        os._exit(0)
    fo = open("login-time", "w")
    fo.write(str(int(time.time())))
    # 关闭打开的文件
    fo.close()
print("登录手机号为：", phone)
print("预约项，和日期为", selectData)

def worke(select):
    listType = False
    # 获取预约列表
    while (listType == False):
        list = listClass.List(sessionId)
        listData = list.getList()
        for l in listData:
            # 判断是否为预约信息
            if l['title'] == select['title']:
                listType = True
                info = l
        if listType == False:
            print('休眠', config.LIST_WAIT, '秒')
            time.sleep(config.LIST_WAIT)
    # 获取详情
    detailType = False
    while (detailType == False):
        detail = detailClass.Detail(sessionId, info['url'], select)
        detailInfo = detail.getDetail()
        if len(detailInfo['date']) > 0 :
            detailType = True
        if detailType == False:
            print('休眠', config.DETAIL_WAIT, '秒')
            time.sleep(config.DETAIL_WAIT)
    bookTime = 0
    bookStatus = False
    while (bookStatus == False):
        for date in detailInfo['date']:
            handle = handleClass.Handle(sessionId, detailInfo, people, date, info)
            bookStatus = handle.book()
            if bookStatus == False:
                bookTime += 1

        if bookTime > config.BOOK_RETRY_TIME:
            print('重试', config.BOOK_RETRY_TIME, '次，还未成功，结束脚本')
            return
        if bookStatus == False:
            print('休眠', config.BOOK_WAIT, '秒')
            time.sleep(config.BOOK_WAIT)

#  开启线程
# thres = [Thread(target=worke, args=(t,))
#             for t in selectData]
# # 开始执行线程
# [thr.start() for thr in thres]
# # 等待线程执行结束
# [thr.join() for thr in thres]

def main():
    if len(selectData) > 10:
        print("最多可以同时抢十个")
        os._exit(0)
    for t in selectData:
        worke(t)
if __name__ == '__main__':
    main()