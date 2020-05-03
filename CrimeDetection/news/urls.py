from django.urls import include, path, re_path
from django.views.generic import ListView, DetailView
from news.models import Articles
from django.views.generic import ListView
from django.views.generic.detail import DetailView
urlpatterns = [
   re_path(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],template_name="news/posts.html")),
]


