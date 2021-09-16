from django.shortcuts import render
from .models import Project

#redirect home page requests to home.html
def home(request):
    projects = Project.objects.all() #grabs all objects from models
    return render(request, 'portfolio/home.html', {'projects':projects})
