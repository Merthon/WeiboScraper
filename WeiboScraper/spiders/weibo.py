import scrapy
from scrapy_redis.spiders import RedisSpider
from WeiboScraper.items import WeiboItem
from urllib.parse import parse_qs, urlparse

class WeiboSpider(RedisSpider):
    name = 'weibo'
    allowed_domains = ['s.weibo.com']
    redis_key = 'weibo:start_urls'

    def parse(self, response):
        if response.status != 200:
            print(f"Error: {response.url} 返回 {response.status}")
            return
        print("URL:", response.url)
        topic = parse_qs(urlparse(response.url).query).get('q', ['unknown'])[0]
        posts = response.css('div.card-wrap')
        for post in posts:
            try:
                item = WeiboItem()
                item['user_id'] = post.css('a.name::attr(href)').get(default='unknown').split('/')[-1].split('?')[0]
                item['nickname'] = post.css('a.name::text').get(default='unknown')
                item['content'] = ''.join(post.css('p.txt::text').getall()).strip() or 'N/A'
                item['post_time'] = post.css('p.from a:first-child::text').get(default='N/A').strip()
                item['likes'] = post.css('span.woo-like-count::text').get(default='0')
                item['topic'] = topic
                yield item
            except Exception as e:
                print(f"解析错误: {e}")

        # 下一页
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)