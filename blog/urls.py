"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('search/',views.search,name="search")
]