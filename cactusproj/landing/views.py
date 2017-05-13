# from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from .forms import ProblemCreateForm


class MainPageView(LoginRequiredMixin, CreateView):
    template_name = 'landing/main_page.html'
    form_class = ProblemCreateForm

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        return super(MainPageView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, _('Problem created successfully'))
        return reverse_lazy('landing:main_page')


class MapPageView(LoginRequiredMixin, TemplateView):
    template_name = 'landing/map_page.html'
