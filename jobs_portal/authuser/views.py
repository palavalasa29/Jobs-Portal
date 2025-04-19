from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from hr.models import Hr

# Create your views here.

def register_candidate(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password != password_confirm:
            msg = "Passwords do not match!"
            return render(request, 'authuser/candidateRegisteration.html', {'msg': msg})
        if User.objects.filter(username = username).exists():
            msg = "Username already taken"
            return render(request, 'authuser/candidateRegisteration.html', {'msg': msg})
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('candidate_dashboard')
    return render(request, 'authuser/candidateRegisteration.html')

def register_hr(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password != password_confirm:
            msg = "Passwords do not match!"
            return render(request, 'authuser/hrRegisteration.html', {'msg': msg})
        if User.objects.filter(username = username).exists():
            msg = "Username already taken"
            return render(request, 'authuser/hrRegisteration.html', {'msg': msg})
        user = User.objects.create_user(username, email, password)
        Hr(user=user).save()
        login(request, user)
        return redirect('hrHome')
    return render(request, 'authuser/hrRegisteration.html')

def login_user(request):
    msg = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            if Hr.objects.filter(user=user).exists():
                return redirect('hrHome')
            return redirect('candidate_dashboard')
        else:
            msg = "Username or Password are no valid!"
    return render(request, 'authuser/login.html', {'msg': msg})

def logout_user(request):
    logout(request)
    return redirect('login')
