from django.shortcuts import render, redirect
from hr.models import JobPost, candidateApplication, selectedCandidate, Hr
from django.contrib.auth.decorators import login_required
from candidate import views

# Create your views here.


@login_required
def hrHome(request):
    if Hr.objects.filter(user = request.user).exists():
        jobPosts = JobPost.objects.filter(user = request.user)
        return render(request, 'hr/hrdashboard.html', {'jobPosts': jobPosts})
    return redirect('candidate_dashboard')


@login_required
def post_job(request):
    msg = None
    if request.method == "POST":
        job_title = request.POST.get("jobtitle")
        location = request.POST.get("location")
        companyName = request.POST.get("companyName")
        salary = request.POST.get("salary") 
        lastDateToApply = request.POST.get("lastDateToApply")
        job_post = JobPost(user = request.user, title = job_title, location = location, companyName=companyName, salary = salary, lastDateToApply = lastDateToApply)
        job_post.save()
        msg = "Job post added successfully"
        return redirect('hrHome')
    return render(request, 'hr/postjob.html', {'msg': msg})


@login_required
def candidate_view(request, id):
    if JobPost.objects.filter(id = id).exists():
        job = JobPost.objects.get(id = id)
        applications = candidateApplication.objects.filter(job = job)
        selected_applications = selectedCandidate.objects.filter(job = job)
        return render(request, 'hr/candidate.html', {'applications': applications, 'selected_applications': selected_applications, 'jobpost': job})
    return render(request, 'hrHome')

@login_required
def selectCandidate(request):
    if request.method == "POST":
        candidateId = request.POST.get('candidateid') 
        jobId = request.POST.get('jobpostid')

        job = JobPost.objects.get(id=jobId)
        candidate = candidateApplication.objects.get(id=candidateId)

        if selectedCandidate.objects.filter(candidate=candidate, job=job).exists():
            return redirect("hrHome")

        selectedCandidate(job=job, candidate=candidate).save()

    return redirect('hrHome')


@login_required
def deleteCandidate(request):
    if request.method == "POST":
        candidateId = request.POST.get('candidateid') 
        jobId = request.POST.get('jobpostid')
        job = JobPost.objects.get(id = jobId)
        candidateApplication.objects.get(id = candidateId).delete()
        job.applyCount -= 1
        job.save()
    return redirect('hrHome')
