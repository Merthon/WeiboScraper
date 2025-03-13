import scrapy

class WeiboItem(scrapy.Item):
    user_id = scrapy.Field()
    nickname = scrapy.Field()
    content = scrapy.Field()
    post_time = scrapy.Field()
    likes = scrapy.Field()
    topic = scrapy.Field()