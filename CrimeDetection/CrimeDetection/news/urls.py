from django.urls import include, path, re_path
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from news.models import Articles
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],template_name="news/posts.html")),
   url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles,template_name="news/post.html")),
 
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)