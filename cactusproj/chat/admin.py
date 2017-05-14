from django.contrib import admin

# Register your models here.
from .models import Message, Thread


@admin.register(Message)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'sender', 'receiver', 'created_at', 'thread', 'message')
    list_filter = ('sender', 'receiver')
    search_fields = ('sender', 'receiver')
    list_display_links = ('pk', 'sender', 'receiver')


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_message_text', 'last_message_time', 'show_participants')
    filter_horizontal = ('participants',)
    list_display_links = ('pk', 'last_message_text', 'last_message_time')