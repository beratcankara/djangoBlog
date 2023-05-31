from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('addArticle/', views.addArticle,name="addArticle"),
    path('editArticle/<int:article_id>/', views.editArticle,name="editArticle"),
    path('deleteArticle/<int:article_id>', views.delete_articles, name='deleteArticle'),
    path('publishArticle/<int:article_id>', views.publishArticle,name="publishArticle"),
    path('article/<int:article_id>', views.showArticle,name="showArticle"),
    
    
]