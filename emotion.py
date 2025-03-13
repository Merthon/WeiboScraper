from pymongo import MongoClient
from snownlp import SnowNLP

client = MongoClient('localhost', 27017, username='admin', password='admin')
db = client['weibo_db']
posts = list(db.posts.find())

sentiments = [SnowNLP(post['content']).sentiments for post in posts]
avg_sentiment = sum(sentiments) / len(sentiments)
pos_rate = sum(1 for s in sentiments if s > 0.5) / len(sentiments)
print(f"平均情感: {avg_sentiment:.2f}, 正面比例: {pos_rate:.2%}")