from django.urls import path
from FilmyApp import views
urlpatterns = [
    path('', views.home),
    path('aboutus/', views.about,name='aboutus'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('news_events/', views.news_events,name='news_events'),
    path('ideas/', views.contact,name='ideas'),
    path('careers/', views.career,name='careers'),
    path('blogs/',views.blogs,name='blogs'),
    #dropdown 
    path('collaborations/', views.collaboration,name='collaborations'),
    path('fansinteraction/', views.fansinteraction,name='fansinteraction'),
    path('sponsorship/', views.sponsorship,name='sponsorship'),  
    path('enquiries/', views.shows_productions, name='enquiries'),
   
  
    
    #carrer pages 
    path('assistent_director/', views.assistent_director, name='assistent_director') ,   
    path('tvproducer/', views.tv_producer, name='tv_producer'), 
    path('unit_production/', views.unit_production, name='unit_production'), 
    path('apply/', views.Apply_job, name='apply'), 

    path('production/', views.production_page_1, name='production'), 
    path('show/', views.show_page_1, name='show'), 
    

]
