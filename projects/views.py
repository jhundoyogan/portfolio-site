from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    project = Project.objects
    return render(request, 'projects/home.html', {'projects': project})
