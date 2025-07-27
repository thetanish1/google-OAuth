from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'home.html')


def home(request):
    return render(request,"home.html")


def logout_view(request):
    logout(request)
    return redirect("/login")


