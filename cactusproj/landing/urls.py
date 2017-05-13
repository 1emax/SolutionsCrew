from django.conf.urls import url

from .views import (
    MainPageView, MapPageView
)

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='main_page'),
    url(r'^map/$', MapPageView.as_view(), name='map_page'),
]
