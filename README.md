# WeiboScraper
分布式微博爬虫 + 数据分析API

## 功能
- **爬取**：抓取微博热门话题、用户信息、帖子内容。
- **存储**：数据存MongoDB，包含用户ID、昵称、内容、时间、点赞、话题。
- **分析**：词频统计（jieba）、情感分析（snownlp）。
- **API**：FastAPI后端，提供帖子和用户信息查询。

## 技术栈
- Python
- Scrapy（爬虫框架）
- Scrapy-Redis（分布式支持）
- FastAPI（后端API）
- MongoDB（数据存储）
- jieba（中文分词）
- snownlp（情感分析）

## 部署
1. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   brew install redis  # Mac安装Redis
2. **更改配置**：
   settings copy.py -> setting.py
3. **启动redis**
   ```redis-cli
   LPUSH weibo:start_urls "微博话题链接"
   LPUSH weibo:start_urls "微博话题链接"
4. **运行爬虫**
   ```bash
   scrapy crawl weibo
5. **运行API**
   ```bash
   uvicorn api:app --reload
## 博客
https://merthon.github.io/
   
