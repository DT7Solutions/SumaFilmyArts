from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"uifiles/home.html")
def about(request):
    return render (request,"uifiles/about.html")
def portfolio(request):
    return render (request,"uifiles/portfolio.html")
def news_events(request):
    return render (request,"uifiles/news_events.html")
def contact(request):
    return render (request,"uifiles/contact.html")