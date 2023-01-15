from email.headerregistry import Address
from django.shortcuts import render,redirect
from FilmyApp.models import ContactData, Application,Ideas,Sponsorship,Collaboration
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import os
# Create your views here.
def home(request):
    return render (request,"uifiles/home.html",{'navbar':'home'})
def about(request):
    return render (request,"uifiles/about.html",{'navbar':'about'})
def portfolio(request):
    return render (request,"uifiles/portfolio.html",{'navbar':'portfolio'})
def news_events(request):
    return render (request,"uifiles/news_events.html",{'navbar':'news_events'})


def career(request):
    return render (request,"uifiles/career.html",{'navbar':'career'})

def fansinteraction(request):
    return render (request,"uifiles/fansinteraction.html",{'navbar':'collaboration'})

def collaboration(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        brand_agency = request.POST.get('brand',"")
        industry = request.POST.get('industry',"")
        collaboration_Type = request.POST.get('Collaboration_Type',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)
        
        oApplication = Collaboration(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Brand_Agency=brand_agency ,Industry=industry ,file=up_file ,Collaboration_Type=collaboration_Type)
        oApplication.save()
 
        subject="sumfilmyart"
        sucess =f'hi {lastname} Your message has been received, We will contact you soon'
        
        message ='''
        Subject:{}
        Message:{}
        From:{}
        '''.format(subject,sucess,email)
        try:
            mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
            mail.attach_file(upload_file)
            # mail.attach(up_file.name, up_file.read(), up_file.content_type)
            mail.send()
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')
    return render (request,"uifiles/collaboration.html",{'navbar':'collaboration'})



def sponsorship(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        brand_agency = request.POST.get('brand',"")
        industry = request.POST.get('industry',"")
        sponcer_kind = request.POST.get('Kind_Sponcer',"")
        sponcer_type = request.POST.get('Sponcer_Type',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)
        oApplication = Sponsorship(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Brand_Agency=brand_agency ,Industry=industry ,Kind_Sponcer=sponcer_kind,file=up_file ,Sponcer_Type=sponcer_type)
        oApplication.save()
        
        subject="sumfilmyart"
        message =f'hi {firstname} Your Application has been submited Sucessfully'
        
        try:
            # bio_file = io.BytesIO(up_file.read().encode('utf8'))
            mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
            mail.attach_file(upload_file)
            mail.send()
           
        except:
            messages.ERROR(request,'sending fail')

    return render (request,"uifiles/sponsorship.html",{'navbar':'sponsorship'})
 
#enquiries
def shows_productions(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname =  request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        
        oContactinfo = ContactData(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Subject=subject,Message=message)
        oContactinfo.save()
        sucess =f'hi {lastname} Your message has been received, We will contact you soon'
        
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
    return render (request,"uifiles/shows-productions.html",{'navbar':'shows_productions'})


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

def page_not_found_view(request, exception):
    return render(request, 'uifiles/404.html', status=404)

#your ideas form #
def contact(request):
    if request.method == "POST":
        name = request.POST.get('fname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)

        oContactinfo = Ideas(Name=name,Email=email,Phone=phone,Subject=subject,file = up_file)
        oContactinfo.save()

        subject="sumfilmyart"
        message =f'hi {name} Your Application has been submited Sucessfully'
        
        
       
       
        try:
            mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
            mail.attach_file(upload_file)
            # mail.attach(up_file.name, up_file.read(), up_file.content_type)
            mail.send()
           
        except:
            messages.ERROR(request,'sending fail')
     
    return render (request,"uifiles/contact.html",{'navbar':'contact'})
    




# def Apply_job(request):
#     if request.method == "POST":
#         name = request.POST.get('name',"")
#         email = request.POST.get('email',"")
#         phone = request.POST.get('phone',"")
#         address = request.POST.get('address',"")
#         experinces = request.POST.get('inpuexperices',"")
#         message = request.POST.get('message',"")
        # file = request.POST.get('message',"")
        # up_file = request.FILES['file']
        # tr_check = request.POST.get('check'," ")
        # agrement=''
        # if tr_check =="on":
        #     agrement = 'True'
        # oApplication = Application(Name=name,Email=email,Phone=phone,Address=address,Experience =experinces ,Message=message, file=up_file ,Term_check=agrement)
        # oApplication.save()
        # subject="sumfilmyart"
        # sucess =f'hi {name} Your Application has been submited Sucessfully'
        
        # try:
            # bio_file = io.BytesIO(up_file.read().encode('utf8'))
    #         mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
    #         mail.attach(up_file.name, up_file.read(), up_file.content_type )
    #         mail.send()
    #         messages.success(request,sucess)
    #     except:
    #         messages.ERROR(request,'sending fail')
                    
    # return render (request, "uifiles/carrerpages/applyform.html")














# def sending_email(subject, message, email,file):
#     email = EmailMessage(
#     'Hello',
#     'Body goes here',
#     'from@example.com',
#     ['to1@example.com', 'to2@example.com'],
#     ['bcc@example.com'],
#     reply_to=['another@example.com'],
#     headers={'Message-ID': 'foo'},
# )
#     return ""