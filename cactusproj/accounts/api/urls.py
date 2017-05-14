from django.conf.urls import url
from .views import (
    ChangeLikedProblemView
)


urlpatterns = [
    url(r'^like/problem/$', ChangeLikedProblemView.as_view(), name='likedproblem_change'),
]
