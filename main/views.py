from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
# Create your views here.
from django.shortcuts import reverse
from .forms import ContactForm
from django.core.mail import send_mail
from beststroy.settings import DEFAULT_TO_EMAIL, EMAIL_HOST_USER


def tender(request):
    tender = Tender.objects.all()
    context = {
        'tender': tender,
    }
    return render(request, 'pages/tenders.html', context)


def tender_detail(request, slug):
    tender = Tender.objects.get(slug=slug)
    all_tender = Tender.objects.all()
    tender.view_count = tender.view_count + 1
    tender.save()
    context = {
        'tender': tender,
        'all_tender': all_tender,
    }
    return render(request, 'pages/tender_detail.html', context)


def about(request):
    about = About.objects.all()

    context = {
        'about': about,
    }
    return render(request, 'pages/about.html', context)


def projects(request):
    projects = Projects.objects.filter(projects=True).order_by('order')
    context = {
        'projects': projects,
        'set': set,
    }
    return render(request, 'pages/project-category.html', context)


def completed_job(request):
    projects = Projects.objects.filter(completed_job=True).order_by('order')
    context = {
        'projects': projects,
        'set': set,
    }
    return render(request, 'pages/completed_job.html', context)


def new_developments(request):
    projects = Projects.objects.filter(new_developments=True).order_by('order')
    context = {
        'projects': projects,
        'set': set,
    }
    return render(request, 'pages/new_developments.html', context)


def know_how(request):
    projects = Projects.objects.filter(know_how=True).order_by('order')
    context = {
        'projects': projects,
        'set': set,
    }
    return render(request, 'pages/know_how.html', context)


def project_detail(request, slug):
    project = Projects.objects.get(slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'pages/project_detail.html', context)


def news(request):
    news = News.objects.filter(news=True).order_by('order')
    context = {
        'news': news,
    }
    return render(request, 'pages/news.html', context)


def events(request):
    news = News.objects.filter(events=True).order_by('order')
    context = {
        'news': news,
    }
    return render(request, 'pages/events.html', context)


def news_detail(request, slug):
    news = News.objects.get(slug=slug)
    popular_news = News.objects.all().order_by('-order')[:4]
    context = {
        'news': news,
        'popular_news': popular_news,
    }
    return render(request, 'pages/news_detail.html', context)


def membership(request):
    membership = Membership.objects.all()
    context = {
        'membership': membership,
    }
    return render(request, 'pages/membership.html', context)


def membership_page(request, slug):
    membership = Membership.objects.get(slug=slug)
    context = {
        'membership': membership,
    }
    return render(request, 'pages/membership_detail.html', context)


def production(request):
    production = Projects.objects.filter(production=True)
    context = {
        'production': production,
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

            return redirect('thanks')

        else:
            print(form.errors)
    return render(request, 'pages/contact.html', {'form': form})


def tables(request):
    table = Tables.objects.all()
    context = {
        'table': table,
    }
    return render(request, 'pages/table.html', context)


# Static Content Page
def static_content(request, slug):
    param = request.GET.get('cat_name')
    try:
        category = Category.objects.get(slug=param)
        if category.parent is not None:
            static_all = Category.objects.filter(parent=category.parent)
        else:
            static_all = category.get_children()
    except:
        category = None
        static_all = None
    static = StaticContent.objects.get(slug=slug)
    print('statik:==================================================', static_all)
    print('statik:==================================================', static)
    context = {
        'static': static,
        'static_all': static_all,

    }
    return render(request, 'pages/static/static_page.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            projects = Projects.objects.all().filter(
                Q(translations__description__icontains=keyword) | Q(translations__title__icontains=keyword))
    context = {
        'projects': projects,
        # 'product_count': product_count,
    }
    return render(request, 'pages/project-category.html', context)


def citizen(request):
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

            return redirect('thanks')

        else:
            print(form.errors)
    return render(request, 'pages/citizen.html', {'form': form})


def kartel(request):
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

            return redirect('thanks')

        else:
            print(form.errors)
    return render(request, 'pages/kartel.html', {'form': form})


def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery,
    }
    return render(request, 'pages/gallery.html', context)


def video(request):
    video = Video.objects.all()
    context = {
        'video': video,
    }
    return render(request, 'pages/video.html', context)


def thanks(request):
    return render(request, 'includes/thanks.html')


def category(request):
    cat = Category.objects.all()
    context = {
        'cat': cat,
    }
    return render(request, 'includes/header.html', context)


def blogpage(request):
    return render(request, 'pages/blog.html')