from django.conf.urls import url

from .views import UserChatView, MessageOverview

urlpatterns = [
    url(r'^$', MessageOverview.as_view(), name='chat_overview'),
    url(r'^(?P<slug>[-\w]+)/$', UserChatView.as_view(), name='personal_chat'),
]
