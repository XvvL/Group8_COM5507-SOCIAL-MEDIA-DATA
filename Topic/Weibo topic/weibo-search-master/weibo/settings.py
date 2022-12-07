# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 10
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': 'SINAGLOBAL=4092238210759.6934.1663399482024; _ga=GA1.2.418912749.1670045443; UOR=,,m.weibo.cn; SSOLoginState=1670253040; _s_tentry=weibo.com; Apache=6652837918480.82.1670253045290; ULV=1670253045411:3:3:2:6652837918480.82.1670253045290:1670210711845; XSRF-TOKEN=FcqNDCqTLqMBXxlGKrEngwmK; WBPSESS=QMejCazxEeedFzO4BSGcH794s0cxd2OrNTpQTtPVwOyUoWSqwC0wtRfhej1GZh3cwa-LUJ_L2UEWSaq5kjh20pqjXSkiDN9r4hvmSRZn-yvXresgE6se_5SvLurwRoxSTutSnu-58UVPE-F9Or0swA==; PC_TOKEN=23ebca11b5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWyVcNdwzAXHzZLmcybSX1X5JpX5KMhUgL.FozfSo5p1K-f1Kz2dJLoIp7LxK-L12qL1KMLxK.LBKeL12-LxK-L1K5LBoLk; ALF=1672931611; SCF=AmnYV__X6CIe9iKPZBtOyKLUIAWmJs-_VDORHCmUkg6-tCxK2Bg5MnjAm2YKrkK7QijXi03mxPA_OmYTOmhwX0E.; SUB=_2A25OiyxNDeRhGeRL7VIQ-SvJwj6IHXVt4RqFrDV8PUNbmtANLUTCkW9NUyQKonxidEa74xEnL6cVnDMkX30qOTNd'
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['乌克兰']  # 或者 KEYWORD_LIST = 'keyword_list.txt'
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0

# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2022-03-01'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2022-03-01'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 46


