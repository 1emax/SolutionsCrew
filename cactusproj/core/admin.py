from django.contrib import admin

from .models import Problem, Institution, InstitutionProblem, SocialGroup


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(InstitutionProblem)
class InstitutionProblemAdmin(admin.ModelAdmin):
    list_display = ['status']


@admin.register(SocialGroup)
class SocialGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
