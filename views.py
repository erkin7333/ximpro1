from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
# Create your views here.
from django.shortcuts import reverse
from .forms import ContactForm
from django.core.mail import send_mail
from beststroy.settings import DEFAULT_TO_EMAIL, EMAIL_HOST_USER

def about(request):
    home_images = HomeImages.objects.all()

    context = {
        'home_images':home_images,
    }
    return render(request, 'pages/about.html', context)


def projects(request):
    projects = Projects.objects.filter(projects=True)
    context = {
        'projects':projects,
    }
    return render(request, 'pages/project-category.html', context)


def project_detail(request, slug):
    project = Projects.objects.get(slug=slug)
    images = ProjectsImages.objects.filter(project=project.id)
    context = {
        'project':project,
        'images':images,
    }
    return render(request, 'pages/project_detail.html', context)

def services(request):
    services = Services.objects.all()
    context = {
        'services':services,
    }
    return render(request, 'pages/services.html', context)

def service_detail(request, slug):
    service = Services.objects.get(slug=slug)
    images = ProjectsImages.objects.filter(service=service.id)
    context = {
        'service':service,
        'images':images,
    }
    return render(request, 'pages/service_detail.html', context)


def production(request):
    production = Projects.objects.filter(production=True)
    context = {
        'production':production,
    }
    return render(request, 'pages/production.html', context)


def certificate(request):
    return render(request, 'pages/certificates.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            theme = request.POST.get('theme')
            message = request.POST.get('message')


            message = f"From: {name} \n email: {email} \n phone: {phone} \n theme: {theme} \n message: {message}"

            send_mail('Contact', message, EMAIL_HOST_USER, [DEFAULT_TO_EMAIL])

            return render(request, "pages/contact.html", {'thanks': True})
    
        else:
            print(form.errors)
    return render(request, 'pages/contact.html', {'form': form})