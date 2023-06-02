from django.contrib import admin
from django.urls import path,include
from articles import views
from . import views as mainViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.index,name="index"),
    path('countries/', include("medium.urls")),
    path('about/', views.about,name="about"),
    path('user/', include("user.urls")),
    path('dashboard/', include("articles.urls")),
    path('search/',views.search,name="search"),
    path('deleteComment/<int:commentId>',mainViews.deleteComment,name="deleteComment"),
    path('editComment/<int:commentId>',mainViews.editComment,name="editComment"),
    
    
]
