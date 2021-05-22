from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Academic)
class AcademicDisplay(admin.ModelAdmin): 
    list_display = ['user','degree','year','college','board','percentage']

@admin.register(ExtraCurriculam)
class ExtraCurriculamDisplay(admin.ModelAdmin): 
    list_display = ['user','certificate','offered_By','year']

@admin.register(Experience)
class ExperienceDisplay(admin.ModelAdmin): 
    list_display = ['user','company_name','role','starting_date','currently_Working','end_date','Description']

@admin.register(Skill)
class SkillData(admin.ModelAdmin): 
    list_display = ['user','languages','Version']

@admin.register(Interested_Area)
class Interested_AreaDisplay(admin.ModelAdmin): 
    list_display = ['user','Interested']

@admin.register(Project)
class ProjectDisplay(admin.ModelAdmin): 
    list_display = ['user','project_name','gitUrl','Description']

@admin.register(Hobby)
class HobbyDisplay(admin.ModelAdmin): 
    list_display = ['user','Interested']

@admin.register(CareerObjective)
class careerObjectiveDisplay(admin.ModelAdmin):
    list_display = ['user','objective']