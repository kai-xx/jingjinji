## 京津冀一卡通， 自助预约脚本

1. 克隆项目
2. cp config.demo.py config.py 修改相应项
3. 安装requirements.txt中依赖
4. python run.py

---

## 关于如何获取SESSION_ID
1. 通过pc端抓包工具，获取header中 ```Cookie: JSESSIONID=xxxxxxxxxxx```
2. 通过手机APP抓包工具获取 IOS： stream， android 自行google 百度