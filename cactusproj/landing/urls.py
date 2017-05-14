from django.conf.urls import url

from .views import (
    MainPageView, MapPageView, ProblemDetailView, FeedPageView
)

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main_page'),
    url(r'^map/$', MapPageView.as_view(), name='map_page'),
    url(r'^feed/$', FeedPageView.as_view(), name='feed_page'),
    url(r'^problem/(?P<pk>\d+)/$', ProblemDetailView.as_view(), name='problem_detail'),
]
