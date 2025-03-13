from pymongo import MongoClient

class WeiboScraperPipeline:
    def __init__(self):
        self.client = MongoClient('localhost', 27017, username='admin', password='admin')
        self.db = self.client['weibo_db']
        self.collection = self.db['posts']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()