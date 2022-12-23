from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
# Create your views here.

def home(request):
    banner = Banner.objects.all()
    projects = Projects.objects.all()
    news = News.objects.all()
    context = {
        'banner':banner,
        'projects':projects,
        'news':news,
    }
    return render(request, 'home.html', context)