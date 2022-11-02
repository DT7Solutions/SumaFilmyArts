from django.contrib import admin
from .models import ContactData, Application
# Register your models here.
class  AdminContactData(admin.ModelAdmin):
    list_display=('Name','Email' ,'Phone','Subject','Message')

#for application form 
class AdminApplication(admin.ModelAdmin):
    list_display=('Name','Email' ,'Phone','Address','Experience','Message','file','Term_check')

admin.site.register(ContactData,AdminContactData)
admin.site.register(Application,AdminApplication)


