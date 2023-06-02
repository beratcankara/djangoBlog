from django.contrib import admin
from .models import Article, Comment

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    search_fields = ["title"]
    list_filter=["created_date","author"]
    class Meta:
        model = Article
        
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "user", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["user__username"]