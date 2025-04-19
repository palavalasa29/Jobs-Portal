from django.contrib import admin
from candidate import models

# Register your models here.
@admin.register(models.appliedJobList)
class appliedJobListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'dateApplied')

@admin.register(models.IsSortList)
class IsSortListtAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'dateApplied')

