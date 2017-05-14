from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from imagekit.processors import Adjust, ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField
from django.utils.translation import ugettext_lazy as _
from cactusproj.utils.model_utils import UploadToPathAndRename


class ProblemQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=1)


class Problem(models.Model):
    '''
        Here is problem models in which we will be storing all city problems
        starting from holes in roads, broken city lights and etc
    '''
    STATUS_CHOICES = (
        (1, _('active')),
        (0, _('passive')),
        (None, _('unknown'))
    )
    name = models.CharField(max_length=256, blank=False, null=False)
    image = ProcessedImageField(
        upload_to=UploadToPathAndRename('problem_images'),
        processors=[
            ResizeToFill(400, 400),
            Adjust(sharpness=1.1, contrast=1.1)],
        format='JPEG',
        options={'quality': 70}, null=True, blank=True
    )
    description = models.TextField(blank=False, null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    location = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        help_text=_('field for storing photo location')
    )
    upload_date = models.DateTimeField(help_text=_('date when photo was made/uploaded'))
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        blank=True, null=True,
        help_text=_('state in which our problem is currently')
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = ProblemQuerySet.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('landing:problem_detail', kwargs={'pk': self.id})

    image_xs = ImageSpecField(
        source='image',
        processors=[ResizeToFill(32, 32)],
        format='JPEG',
        options={'quality': 80}
    )


class Institution(models.Model):
    '''
        Here is model for institution
        Here will be institutions to which we will be reporting problems
        Some government institutions or etc
    '''
    STATUS_CHOICES = (
        (1, _('active')),
        (0, _('passive')),
        (None, _('unknown'))
    )
    name = models.CharField(max_length=256, blank=False, null=False)
    url = models.URLField(
        max_length=200,
        blank=False, null=False,
        help_text=_('url of institution')
    )
    description = models.TextField(blank=False, null=False)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        blank=True, null=True,
        help_text=_('active or passive')
    )
    problems = models.ManyToManyField(Problem, through='InstitutionProblem')

    def __str__(self):
        return self.name


class InstitutionProblem(models.Model):
    STATUS_CHOICES = (
        (2, _('resolved')),
        (1, _('ignored')),
        (0, _('started')),
        (None, _('unknown'))
    )
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        blank=True, null=True,
        help_text=_('active or passive')
    )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class SocialGroup(models.Model):
    '''
        Here will be vk, fb groups to which we will be promoting problems
        in order to get government's attention
    '''
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    url = models.URLField(
        max_length=200,
        blank=False, null=False,
        help_text=_('url for social group')
    )

    def __str__(self):
        return self.name
