from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False) 

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)