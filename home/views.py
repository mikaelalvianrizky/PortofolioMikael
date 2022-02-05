from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'index.html')

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_details.html', {'project': project})

def ml_project(request):
    return render(request, 'ml_project.html')

def webdev_project(request):
    return render(request, 'webdev_project.html')

def app_project(request):
    return render(request, 'app_project.html')