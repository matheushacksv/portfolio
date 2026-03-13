from django.shortcuts import render
from .models import Project, Experience


def home(request):

    top_projects = Project.objects.filter(personal_rating__gt=7).order_by('-personal_rating')[:3]

    context = {
        'top_projects': top_projects
    }

    return render(request, 'index.html', context)

def projects_view(request):

    projects = Project.objects.all()
    total_projects = Project.objects.count()

    context = {
        'projects': projects,
        'total_projects': total_projects
    }
    
    return render(request, 'projects.html', context)


def sobre_view(request):

    experiences = Experience.objects.all()

    context = {
        'experiences': experiences
    }
    
    return render(request, 'sobre.html', context)


def contact_view(request):
    return render(request, 'contact.html')