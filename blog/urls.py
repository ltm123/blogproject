from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
    url('^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url('^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url('^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # url('^search/$', views.search, name='search'),
]
