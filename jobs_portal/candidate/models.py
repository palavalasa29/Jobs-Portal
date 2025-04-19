from django.db import models
from django.contrib.auth.models import User
from hr.models import candidateApplication, JobPost
# Create your models here.

class appliedJobList(models.Model):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE)
    job = models.ForeignKey(to=candidateApplication, on_delete = models.CASCADE)
    dateApplied = models.DateField(auto_now_add=True)


class IsSortList(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    job = models.OneToOneField(to=JobPost, on_delete=models.CASCADE)
    dateApplied = models.DateField(auto_now_add=True)