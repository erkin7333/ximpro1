from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('know_how/', views.know_how, name='know_how'),
    path('completed_job/', views.completed_job, name='completed_job'),
    path('new_developments/', views.new_developments, name='new_developments'),

    path('projects/<slug:slug>', views.project_detail, name='project_detail'),
    path('news/', views.news, name='news'),
    path('events/', views.events, name='events'),
    path('news/<slug:slug>', views.news_detail, name='news_detail'),
    path('production/', views.production, name='production'),
    path('certificate/', views.certificate, name='certificate'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='project_search'),
    path('citizen/', views.citizen, name='citizen'),
    path('gallery/', views.gallery, name='gallery'),
    path('video/', views.video, name='video'),
    path('kartel/', views.kartel, name='kartel'),
    path('tables/', views.tables, name='table'),
    path('tender/', views.tender, name='tender'),
    path('thanks/', views.thanks, name='thanks'),
    path('membership/', views.membership, name='membership'),
    path('membership/<slug:slug>', views.membership_page, name='membership_page'),
    path('tender/<slug:slug>', views.tender_detail, name='tender_detail'),  
    path('content/<slug:slug>', views.static_content, name='static_page'),
    path('blog/', views.blogpage, name='blogpage')
]
