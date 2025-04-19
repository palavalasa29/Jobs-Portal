from django.contrib import admin
from hr import models 
# Register your models here.

@admin.register(models.Hr)
class HrAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(models.JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'location', 'companyName', 'salary', 'applyCount', 'lastDateToApply')

@admin.register(models.candidateApplication)
class candidateApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job')

@admin.register(models.selectedCandidate)
class selectedCandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'candidate')