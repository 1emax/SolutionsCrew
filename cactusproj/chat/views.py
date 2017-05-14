from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from braces.views import LoginRequiredMixin

from .forms import ChatForm
from .models import Thread


class MessageOverview(LoginRequiredMixin, TemplateView):
    template_name = 'chat/overview.html'

    def get_threads(self):
        threads = self.request.user.threads.active()
        return [[thread.participants.exclude(id=self.request.user.id)[0], thread.last_message_text, thread.last_message_time] for thread in threads]

    def get_context_data(self, **kwargs):
        context = super(MessageOverview, self).get_context_data(**kwargs)
        context['threads'] = self.get_threads()
        return context


class UserChatView(LoginRequiredMixin, FormView):
    template_name = 'chat/user_chat.html'
    form_class = ChatForm
    success_url = reverse_lazy('chat:chat_overview')

    def get_receiver(self):
        if not User.objects.filter(profile__slug=self.kwargs['slug']).exists():
            raise Http404
        else:
            return User.objects.filter(profile__slug=self.kwargs['slug']).first()

    def get_messages(self):
        receiver = User.objects.filter(profile__slug=self.kwargs['slug']).first()
        thread = Thread.objects.filter(participants=receiver).filter(participants=self.request.user).first()
        if thread is None:  # so we initialise Thread
            new_thread = Thread.objects.create()
            new_thread.participants.add(receiver, self.request.user)
            new_thread.save()
            thread = Thread.objects.filter(participants=receiver).filter(participants=self.request.user).first()

        messages = thread.messages.all()[:40][::-1]
        return messages

    def get_context_data(self, **kwargs):
        context = super(UserChatView, self).get_context_data(**kwargs)
        context['receiver'] = self.get_receiver()
        context['messages'] = self.get_messages()
        return context

    def form_invalid(self, form):
        if self.request.is_ajax():
            return render(self.request, 'chat/ajax.html', {'messages': self.get_messages()})

    def form_valid(self, form):
        if self.request.is_ajax():
            new_message = form.save(commit=False)
            new_message.sender = self.request.user
            new_message.receiver = form.cleaned_data['receiver']
            new_message.thread = Thread.objects.filter(participants=form.cleaned_data['receiver']).filter(participants=self.request.user).first()
            new_message.message = form.cleaned_data['message']
            new_message.save()
            return render(self.request, 'chat/ajax.html', {'messages': self.get_messages()})
