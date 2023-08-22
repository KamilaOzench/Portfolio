from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request): #будем принимать request как параметр
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})