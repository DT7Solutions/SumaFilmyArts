from django.urls import path
from FilmyApp import views
urlpatterns = [
    path('', views.home),
    path('about/', views.about,name='about'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('news_events/', views.news_events,name='news_events'),
    path('contact/', views.contact,name='contact'),
]
