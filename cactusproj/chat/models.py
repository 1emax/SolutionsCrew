from django.db import models
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class ThreadManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ThreadManager, self).exclude(messages__isnull=True)


class Thread(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='threads')
    last_message_time = models.DateTimeField(null=True, blank=True, db_index=True)
    last_message_text = models.CharField(max_length=200, null=True, blank=True)

    objects = ThreadManager()

    def show_participants(self):
        return ' - '.join([str(i) for i in self.participants.all()])

    def __str__(self):
        return ' - '.join([str(i) for i in self.participants.all()])

    class Meta:
        ordering = ['-last_message_time']


class MessageManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(MessageManager, self).exclude(thread__time_to_live__gt=timezone.now())


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender_user')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiver_user')
    message = models.CharField(max_length=200)
    thread = models.ForeignKey(Thread, null=True, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.message


def update_last_message_datetime(sender, instance, created, **kwargs):
    """
    Update Thread's last_message field when
    a new message is sent.
    """
    if not created:
        return

    Thread.objects.filter(id=instance.thread.id).update(
        last_message_time=instance.created_at,
        last_message_text=instance.message,
    )


post_save.connect(update_last_message_datetime, sender=Message)