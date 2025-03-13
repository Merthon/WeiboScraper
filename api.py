from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

client = MongoClient('localhost', 27017, username='admin', password='admin')
db = client['weibo_db']

class Post(BaseModel):
    user_id: str
    nickname: str
    content: str
    post_time: str
    likes: str
    topic: str

@app.get("/posts/", response_model=List[Post])
def get_posts(topic: Optional[str] = None, limit: int = 10):
    query = {'topic': topic} if topic else {}
    posts = list(db.posts.find(query).limit(limit))
    return [Post(**post) for post in posts]

@app.get("/posts/{user_id}", response_model=List[Post])
def get_user_posts(user_id: str, limit: int = 10):
    posts = list(db.posts.find({'user_id': user_id}).limit(limit))
    return [Post(**post) for post in posts]