from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from .views import home

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('main/', include('main.urls')),
)

urlpatterns += [
    re_path(r'^rosetta/', include('rosetta.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)