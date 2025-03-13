from pymongo import MongoClient
from collections import Counter
import jieba

client = MongoClient('localhost', 27017, username='admin', password='admin')
db = client['weibo_db']
posts = list(db.posts.find())

all_text = ' '.join(post['content'] for post in posts)
words = jieba.cut(all_text)
word_freq = Counter(words)
print("全局Top 20 词频:", word_freq.most_common(20))

for topic in db.posts.distinct('topic'):
    topic_text = ' '.join(post['content'] for post in db.posts.find({'topic': topic}))
    topic_words = jieba.cut(topic_text)
    print(f"\n话题 {topic} Top 10:", Counter(topic_words).most_common(10))