from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Experience
from .tasks import enviar_email_contato, novo_contato


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

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        assunto = request.POST.get('subject')
        mensagem = request.POST.get('message')

        enviar_email_contato.delay(email)
        novo_contato.delay(email='matheushacksv@gmail.com', email_do_contato=email, name=name, objetivo=assunto, mensagem=mensagem)

        return JsonResponse({'success': True})


    return render(request, 'contact.html')

