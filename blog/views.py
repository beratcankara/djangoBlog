import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import requests
from articles.forms import Comment, CommentForm
from django.contrib.auth.decorators import login_required

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

@login_required
def deleteComment(request, commentId):
    comment = get_object_or_404(Comment, id=commentId)
    # Yorumu silme işlemini gerçekleştirin
    comment.delete()
    # Silme işleminden sonra yapılacak işlemi belirleyin
    return redirect('article')  # Örnek olarak yorumların bulunduğu sayfaya yönlendirme yapabilirsiniz

@login_required
def editComment(request, commentId):
    comment = get_object_or_404(Comment, id=commentId)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        form.save()
        return redirect("index")
    else:
        form = CommentForm(instance=comment)
        context={"form":form}
    return render(request,"editComment.html",context)