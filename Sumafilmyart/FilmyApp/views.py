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

def career(request):
    return render (request,"uifiles/career.html")
def collaboration(request):
    return render (request,"uifiles/collaboration.html")
def fansinteraction(request):
    return render (request,"uifiles/fansinteraction.html")
def sponsorship(request):
    return render (request,"uifiles/sponsorship.html")
def shows_productions(request):
    return render (request,"uifiles/shows-productions.html")
#carrer-pages 
def assistent_director(request):
    return render (request,"uifiles/carrerpages/assistent-director.html")
def tv_producer(request):
    return render (request, "uifiles/carrerpages/tvproducer.html")
def unit_production(request):
    return render (request, "uifiles/carrerpages/unit-production.html")