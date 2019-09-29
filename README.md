## 京津冀一卡通， 自助预约脚本
[![Python Version](https://img.shields.io/badge/python-%3E=3.6.1-brightgreen.svg?maxAge=2592000)](https://www.python.org/)

1. 克隆项目
2. cp config.demo.py config.py 修改相应项
3. 安装requirements.txt中依赖
4. python run.py

---

## 关于如何获取SESSION_ID
1. 通过pc端抓包工具，获取header
2. 通过手机APP抓包工具获取 ```IOS： stream```， android 自行google 百度

## 关于标题问题
1. 可以先执行一次脚本，列表信息会打印出来，然后复制相应```标题```内容，更改配置，再次运行脚本即可。