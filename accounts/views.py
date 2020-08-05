from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    return render(request, 'registration/register.html')

def loginView(request):
    return render(request, 'registration/login.html')

def logoutView(request):
    return render(request, 'registration/logout.html')