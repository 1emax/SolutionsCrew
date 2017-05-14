from django import forms

from .models import Message


class ChatForm(forms.ModelForm):

    class Meta(object):
        model = Message

        fields = (
            'message', 'receiver',
        )
