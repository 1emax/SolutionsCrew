from django import forms

from cactusproj.core.models import Problem


class ProblemCreateForm(forms.ModelForm):

    class Meta(object):
        model = Problem

        fields = (
            # 'name',
            'image',
            # 'description',
            # 'location',
            # 'upload_date',
        )
