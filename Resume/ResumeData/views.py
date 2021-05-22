from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .models import Academic, ExtraCurriculam, Experience, Skill,Interested_Area, Project, Hobby, CareerObjective

# Create your views here.

class Detail(TemplateView):
    template_name = "Detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userData = User.objects.filter(id = context["id"])
        academic= Academic.objects.filter(user = context["id"])
        extraCurriculam = ExtraCurriculam.objects.filter(user = context["id"])
        experience = Experience.objects.filter(user = context["id"])
        skill = Skill.objects.filter(user = context["id"])
        interested_area = Interested_Area.objects.filter(user = context["id"])
        project = Project.objects.filter(user = context["id"])
        hobby = Hobby.objects.filter(user = context["id"])
        careerObjective = CareerObjective.objects.filter(user = context["id"])

        return {
            'userData':userData,
            'careerObjective':careerObjective,
            'academic':academic,
            'extraCurriculam':extraCurriculam,
            'experience':experience,
            'skill':skill,
            'interested_area':interested_area,
            'project':project,
            'hobby':hobby
        }