from email.headerregistry import Address
from django.shortcuts import render,redirect
from FilmyApp.models import ContactData, Application
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Create your views here.
def home(request):
    return render (request,"uifiles/home.html")
def about(request):
    return render (request,"uifiles/about.html")
def portfolio(request):
    return render (request,"uifiles/portfolio.html")
def news_events(request):
    return render (request,"uifiles/news_events.html")


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
def production_page_1(request):
    return render (request, "uifiles/shows-productionpages/production.html")
def show_page_1(request):
    return render (request, "uifiles/shows-productionpages/show.html")


def Apply_job(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        address = request.POST.get('address',"")
        experinces = request.POST.get('inpuexperices',"")
        message = request.POST.get('message',"")
        # file = request.POST.get('message',"")
        up_file = request.FILES['file']
        tr_check = request.POST.get('check'," ")
        agrement=''
        if tr_check =="on":
            agrement = 'True'
        oApplication = Application(Name=name,Email=email,Phone=phone,Address=address,Experience =experinces ,Message=message, file=up_file ,Term_check=agrement)
        oApplication.save()
        subject="sumfilmyart"
        sucess =f'hi {name} Your Application has been submited Sucessfully'
        
        try:
            mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
            mail.attach(up_file.name, up_file.read(), up_file.content_type)
            mail.send()
            messages.success(request,sucess)
        except:
            messages.ERROR(request,'sending fail')
                    
    return render (request, "uifiles/carrerpages/applyform.html")


#contact form submision  #

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        
        oContactinfo = ContactData(Name=name,Email=email,Phone=phone,Subject=subject,Message=message)
        oContactinfo.save()
        sucess =f'hi {name} Your message has been received, We will contact you soon'
        
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,message,email)
        try:
            send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['badugudinesh94@gmail.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')
        #return redirect("/")
    return render (request,"uifiles/contact.html")
    
def sending_email(subject, message, email,file):
    email = EmailMessage(
    'Hello',
    'Body goes here',
    'from@example.com',
    ['to1@example.com', 'to2@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)
    return ""