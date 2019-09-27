# 用户名
USERNAME = ""
# 密码
PASSWORD = ""
# JSESSIONID 自行通过抓包工具获取
# Cookie: JSESSIONID=xxxxxxxxxxx
SESSION_ID = ""
# 京津冀一卡通 绑定用户名称
PEOPLE = ["张三", ]
# 查询 标题 和 日期  最多支持9个
SELECT_DATA = [
    {
        'title': "天津中华曲苑相声会馆（2019）",
        'date': ["2019-09-26"]
    }
]

# 列表重试等待时间
LIST_WAIT = 300

# 详情重试等待时间
DETAIL_WAIT = 120

# 预约重试等待时间
BOOK_WAIT = 30

# 预约重试等待次数
BOOK_RETRY_TIME = 20

# 是否开启 server酱 微信提醒， 使用前需要前往 http://sc.ftqq.com/3.version 扫码绑定获取 SECRET 并关注获得结果通知的公众号
SERVER_CHAN_CONF = {
    "is_server_chan": False,
    "secret": "xxxxx",
}