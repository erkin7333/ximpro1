from .models import SiteSettings, Category


def settings(request):
    settings = SiteSettings.objects.all()
    return {'settings': settings}

def nav(request):
    nav = Category.objects.all()

    return dict(nav=nav)



