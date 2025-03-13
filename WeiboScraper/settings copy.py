# 加入redis
EDIS_HOST = 'localhost'
REDIS_PORT = 6379
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True



BOT_NAME = "WeiboScraper"
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
}

SPIDER_MODULES = ["WeiboScraper.spiders"]
NEWSPIDER_MODULE = "WeiboScraper.spiders"

COOKIES_ENABLED = True
# 伪装浏览器
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': '自己电脑的user-agent',
    'Accept': '浏览器自己F12查看添加',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://s.weibo.com/',
    'Cookie': '登录以后自己的cookie'
}
# 下载延迟，防封
DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS = 8  # redis单机不能太高

# 开启Item Pipeline（后面存MongoDB用）
ITEM_PIPELINES = {
    'WeiboScraper.pipelines.WeiboScraperPipeline': 300,
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

LOG_LEVEL = 'INFO'