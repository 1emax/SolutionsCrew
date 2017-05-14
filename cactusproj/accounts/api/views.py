import math
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
# from django.utils.translation import ugettext as _
from django.http import HttpResponse, QueryDict
from braces.views import LoginRequiredMixin

from cactusproj.core.models import Problem
from cactusproj.accounts.models import LikedProblem, Profile


class ChangeLikedProblemView(LoginRequiredMixin, View):
    def put(self, request, *args, **kwargs):
        try:
            problem_id = int(QueryDict(request.body).get('problem_id'))
            LikedProblem(profile=request.user.profile, problem_id=problem_id).save()
            author = Problem.objects.get(id=problem_id).author
            profile = Profile.objects.get(id=author.id)
            profile.points += 1
            profile.level = int(math.log(profile.points, 2))
            profile.save()
            return HttpResponse("successfully liked problem")
        except Exception as e:
            return HttpResponse("some error occured")

    def delete(self, request, *args, **kwargs):
        try:
            problem_id = int(QueryDict(request.body).get('problem_id'))
            found = LikedProblem.objects.get(profile=request.user.profile, problem_id=problem_id)
            author = Problem.objects.get(id=problem_id).author
            profile = Profile.objects.get(id=author.id)
            profile.points -= 1
            profile.save()
            found.delete()
            return HttpResponse("successfully unliked problem")
        except ObjectDoesNotExist:
            return HttpResponse("some error occured")
