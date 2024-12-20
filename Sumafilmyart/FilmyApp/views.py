from email.headerregistry import Address

from django.shortcuts import render,redirect
from FilmyApp.models import ContactData, Application,Ideas,Sponsorship,Collaboration,Carrers,Blog,GalleryImage,Category
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

def gallery(request):
    gallery_categories = Category.objects.all().order_by('-id')
    gallery_items = GalleryImage.objects.all().order_by('-id')
    return render (request,"uifiles/gallery.html",{'navbar':'gallery', "gallery":gallery_items, "gallery_cat":gallery_categories})
def news_events(request):
    return render (request,"uifiles/news_events.html",{'navbar':'news_events'})
def blogs(request):
    blogs = Blog.objects.filter(status=1).order_by('-id')
    return render (request,"uifiles/blogs.html",{'navbar':'blogs',"blogs":blogs})

def career(request):
    jobdata = Carrers.objects.all()
   
    return render (request,"uifiles/career.html",{'navbar':'career','jobinfo': jobdata})

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
            #    mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , [email])
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
            send_mail(subject, message,'noreplaybadugudinesh94@gmail.com',recipient_list=['team@sumaflimyarts.com']) 
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
            mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , ['team@sumaflimyarts.com'])
            mail.attach_file(upload_file)
            # mail.attach(up_file.name, up_file.read(), up_file.content_type)
            mail.send()
           
        except:
            messages.ERROR(request,'sending fail')
     
    return render (request,"uifiles/contact.html",{'navbar':'contact'})
    




def Apply_job(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        experinces = request.POST.get('userexperices',"")
        up_file = request.FILES['file']
        upload_file = settings.MEDIA_URL[1:] + "//pdf//" + str(up_file.name)
        
        oApplication = Application(FirstName=firstname,LastName=lastname,Email=email,Phone=phone,Experience =experinces, file=up_file )
        oApplication.save()
        subject="JobApplication"
        sucess =f'hi {firstname} Your Application has been submited Sucessfully'
        message ='something'
        try:
            mail = EmailMessage(subject,message, settings.EMAIL_HOST_USER , ['team@sumafilmyarts.com'])
            mail.attach_file(upload_file)
            print('fill attach sucessfully')
            mail.send()
            messages.success(request,sucess)
        except:
            messages.ERROR(request,'sending fail')
                    
    return render (request, "uifiles/carrerpages/applyform.html")

import requests

def linkedin_jobpost(data):
   

    LINKEDIN_API_ENDPOINT = "https://api.linkedin.com/v2/ugcPosts"

    # Define the LinkedIn authentication token
    LINKEDIN_TOKEN = ""

    title = data.get('title')
    loaction = data.get('location')
    description = data.get('description')
   
    payload = {
                
                "author": "urn:li:person:FMT47TxeNx",
                "lifecycleState": "PUBLISHED",
                "specificContent": {    
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": title,
                
                        },
                        # "shareMediaCategory": "NONE"
                        "shareMediaCategory": "ARTICLE",
                        "media": [
                                        {
                                            "status": "READY",
                                            "description": {
                                                "text": loaction
                                            },
                                            "originalUrl": "https://dt7solutions.com",
                                            "title": {
                                                "text":  description
                                            }
                                        }
                                ]
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
        
            }
            
    print("start Post the job posting to LinkedIn")
    response = requests.post(LINKEDIN_API_ENDPOINT, json=payload, headers={"Authorization": f"Bearer {LINKEDIN_TOKEN}"})
    print("sucesfully Post the job posting to LinkedIn")
    return ''



    



   
   












