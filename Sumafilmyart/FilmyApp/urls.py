from django.urls import path
from FilmyApp import views
urlpatterns = [
    path('', views.home),
    path('about/', views.about,name='about'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('news_events/', views.news_events,name='news_events'),
    path('contact/', views.contact,name='contact'),
    path('career/', views.career,name='career'),
    #dropdown 
    path('collaboration/', views.collaboration,name='collaboration'),
    path('fansinteraction/', views.fansinteraction,name='fansinteraction'),
    path('sponsorship/', views.sponsorship,name='sponsorship'),  
    path('shows_productions/', views.shows_productions, name='shows_productions'),
    
    #carrer pages 
    path('assistent_director/', views.assistent_director, name='assistent_director') ,   
    path('tvproducer/', views.tv_producer, name='tv_producer'), 
    path('unit_production/', views.unit_production, name='unit_production'), 
    path('jobapplication/', views.Apply_job, name='jobapplication'), 

    path('production/', views.production_page_1, name='production'), 
    path('show/', views.show_page_1, name='show'), 
    

]
