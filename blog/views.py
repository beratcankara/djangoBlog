import json
import random
from django.shortcuts import render
import requests

from articles.models import Article
def getArticleData():
    url = "https://jsonblob.com/api/jsonBlob/1113201562272153600"
    response = requests.get(url)
    if response.status_code == 200:
        json_datas = response.json()
        return json_datas["articles"]
    else:
        return None    
def index(request):
    articleList = []
    publishedArticles = Article.objects.filter(published=True)  # Yalnızca yayınlanmış makaleleri filtrele
    for article in getArticleData():
        articleId = random.randint(100,250)
        articleTitle = article['title']
        articleContent = article['content']
        articleAuthor = article['author']
        articleInfo = {
            'articleTitle': articleTitle,
            'articleContent': articleContent,
            'articleAuthor': articleAuthor,
            'articleId':articleId,
        }
        articleList.append(articleInfo)
    
    context = {"articleList": articleList,
               "publishedArticles":publishedArticles}
    return render(request, "index.html", context)

