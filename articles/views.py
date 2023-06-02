from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.
def about(request):
    context = {
        "names" : ["Berat", "Can", "Kara"]
    }
    return render(request,"about.html",context=context)
@login_required(login_url="/user/login")
def dashboard(request):
    user = request.user
    articles = Article.objects.filter(author=user)
    article_status = {}  # Makale durumlarını tutacak sözlük

    for article in articles:
        article_status[article.id] = article.published  # Makale durumunu güncelle
    print(article_status)
    context = {
        'articles': articles,
        'article_status': article_status,  # Context'e makale durumlarını ekleyin
    }
    return render(request, 'dashboard.html', context)
@login_required(login_url="/user/login")
def addArticle(request):
    form = ArticleForm
    context={"form":form}
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            content = request.POST.get('content')
            article = Article(title=title,content=content)
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request,"Makaleniz başarıyla eklendi.") 
            return redirect("dashboard")
        else:
            messages.error(request,"Lütfen formları doldurun.")
            return redirect("addArticle")

    else:        
        return render(request,"addArticle.html",context)
    
@login_required
def editArticle(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save() 
            return redirect('dashboard')  # Makale düzenlendikten sonra dashboard sayfasına yönlendir.

    else:
        form = ArticleForm(instance=article)

    return render(request, 'editArticle.html', {'article': form})

@login_required
def delete_articles(request,article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        messages.success(request,"Makaleniz başarıyla silindi.")
        return JsonResponse({'success': True})  # Başarılı bir yanıt döndürün

    return JsonResponse({'success': False})  # Hatalı bir istek olduğunda hata yanıtı döndürün

@login_required
def publishArticle(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        article.published = not article.published
        article.save()
        dashboard(request)

    return redirect('dashboard')
@login_required
def addComment(request,form,article):
    comment = form.save(commit=False)
    comment.article = article
    comment.user = request.user
    comment.save()
    
def showArticle(request,article_id):
    article = Article.objects.filter(id=article_id).first()
    comments = article.comments.all()
    context={
        "article":article
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            addComment(request,form,article)
            return redirect('showArticle', article_id=article_id)
        else:
            messages.error(request,"Lütfen mesaj atmak için giriş yapınız.")
            
    else:
        form = CommentForm()
    
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }
    return render(request, 'article.html', context)

def search(request):
    query = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=query,published = True)
    context = {
        'articles': articles
    }
    return render(request, 'search.html', context)
