from django.contrib import admin

from .models import Problem, Institution, InstitutionProblem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(InstitutionProblem)
class InstitutionProblemAdmin(admin.ModelAdmin):
    list_display = ['status']
