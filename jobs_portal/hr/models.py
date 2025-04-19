from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hr(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

class JobPost(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length=200)
    companyName = models.CharField(max_length=250)
    salary = models.IntegerField(default = 0)
    applyCount = models.IntegerField(default = 0)
    lastDateToApply = models.DateField()  

    def __str__(self):
        return str(self.title)

STATUS_CHOICE = (("pending", "pending"),
                 ("selected", "selected")
                )


class candidateApplication(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    job = models.ForeignKey(to=JobPost, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'job')

    passingYear = models.IntegerField()
    experience = models.IntegerField()
    resume = models.FileField(upload_to="resume/", null=True,blank=True)
    status = models.CharField(choices = STATUS_CHOICE, max_length = 20, default = "pending")

# class selectedCandidate(models.Model):
#     job = models.ForeignKey(to=JobPost, on_delete=models.CASCADE)
#     candidate = models.OneToOneField(to=candidateApplication, on_delete=models.CASCADE)

class selectedCandidate(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    candidate = models.ForeignKey(candidateApplication, on_delete=models.CASCADE)  # Allows multiple selections

