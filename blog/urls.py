from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url('^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]
