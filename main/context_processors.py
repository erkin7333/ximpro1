from .models import SiteSettings, Category, Visit


def settings(request):
    settings = SiteSettings.objects.all()
    return {'settings': settings}

def nav(request):
    nav = Category.objects.all()

    return dict(nav=nav)


def countviews(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    ip_address = request.META['REMOTE_ADDR']
    visit = Visit(ip_address=ip_address)
    visit_count = Visit.objects.filter(ip_address=ip_address).count()
    visit.save()
    return {'visit_count': visit_count, 'num_visits': num_visits}



