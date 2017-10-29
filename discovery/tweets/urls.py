from django.conf.urls import include, url
from django.contrib import admin
from tweets import views
# from .views import tweet_detail_view, tweet_list_view

                    

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.TweetDetailedView.as_view(), name = 'detail'),
    url(r'^$', views.TweetListView.as_view(), name = 'list'),
    url(r'^create/$', views.TweetCreateView.as_view(), name = 'createview'),
    url(r'^(?P<pk>\d+)/edit/$', views.TweetUpdateView.as_view(), name = 'update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TweetDeleteView.as_view(), name = 'delete'),
]

