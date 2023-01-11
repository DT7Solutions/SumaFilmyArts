from django.contrib import admin
from .models import ContactData, Application,ImageUploads,Ideas,Collaboration,Sponsorship

# Register your models here.
class  AdminContactData(admin.ModelAdmin):
    list_display=('FirstName','LastName','Email' ,'Phone','Subject','Message','Date')
    list_filter= ['Date']

#for application form 
class AdminApplication(admin.ModelAdmin):
    list_display=('Name','Email' ,'Phone','Address','Experience','Message','file','Term_check')

class AdminImageuplaods(admin.ModelAdmin):
    list_display=('Name','Image')

class AdminIdeasForm(admin.ModelAdmin):
    list_display=('Name','Email' ,'Phone','Subject','file')
    list_filter= ['Date']

class AdminCollaborationForm(admin.ModelAdmin):
    list_display=('FirstName','LastName','Email' ,'Phone','Brand_Agency','Industry','Collaboration_Type','file')
    list_filter= ['Date']

class AdminSponcershipForm(admin.ModelAdmin):
    list_display=('FirstName','Email' ,'Phone','Brand_Agency','Industry','Kind_Sponcer','Sponcer_Type','file')
    list_filter= ['Date']


admin.site.register(ContactData,AdminContactData)
admin.site.register(Application,AdminApplication)
admin.site.register(ImageUploads,AdminImageuplaods)
admin.site.register(Ideas,AdminIdeasForm)
admin.site.register(Collaboration,AdminCollaborationForm)
admin.site.register(Sponsorship,AdminSponcershipForm)
