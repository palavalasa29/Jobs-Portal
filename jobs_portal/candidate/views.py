from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from hr.models import JobPost, candidateApplication, Hr
from candidate.models import appliedJobList
from django.db import IntegrityError

# Create your views here.



@login_required
def candidate_dashboard(request):
    if Hr.objects.filter(user = request.user).exists():
        return redirect('hrHome')
    jobs = JobPost.objects.all()
    return render(request, 'candidate/dashboard.html', {'jobs': jobs})


@login_required
def jobList(request):
    if Hr.objects.filter(user = request.user).exists():
        return redirect('hrHome')
    jobs = appliedJobList.objects.filter(user = request.user)
    print(jobs)
    return render(request, "candidate/joblist.html", {'jobs': jobs})


@login_required
def apply(request, jobId):
    if Hr.objects.filter(user = request.user).exists():
        return redirect('hrHome')
    if JobPost.objects.filter(id = jobId).exists():
        job = JobPost.objects.get(id = jobId)
        if candidateApplication.objects.filter(user = request.user, job = job):
            return redirect('candidate_dashboard')
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            college = request.POST.get("college")
            passingYear = request.POST.get("passing_year")
            experience = request.POST.get("yearOfExperience")
            resume = request.POST.get("resume")
            about = request.POST.get("about")
            job = JobPost.objects.get(id = jobId)
            if candidateApplication.objects.filter(user = request.user, job = job).exists():
                return redirect('candidate_dashboard')
            else:
                candidate_application = candidateApplication(user = request.user, job = job, passingYear = passingYear, experience = experience, resume=resume)
                candidate_application.save()
                appliedJobList(user = request.user, job = candidate_application ).save()
                job.applyCount += 1
                job.save()
                return redirect('candidate_dashboard')
        return render(request, 'candidate/applyJob.html')
    return render(request, "candidate/applyJob.html")
