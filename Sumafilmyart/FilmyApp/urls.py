from django.urls import path
from FilmyApp import views
urlpatterns = [
    path('', views.home),
    path('about/', views.about,name='about'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('news_events/', views.news_events,name='news_events'),
    path('contact/', views.contact,name='contact'),
    
    path('career/', views.career,name='career'),
    path('collaboration/', views.collaboration,name='collaboration'),
    path('fansinteraction/', views.fansinteraction,name='fansinteraction'),
    path('sponsorship/', views.sponsorship,name='sponsorship'),  
    path('shows_productions/', views.shows_productions, name='shows_productions')  
]
