from django.contrib import admin
from .models import ContactData, Application,ImageUploads
# Register your models here.
class  AdminContactData(admin.ModelAdmin):
    list_display=('FirstName','LastName','Email' ,'Phone','Subject','Message','Date')

#for application form 
class AdminApplication(admin.ModelAdmin):
    list_display=('Name','Email' ,'Phone','Address','Experience','Message','file','Term_check')

class AdminImageuplaods(admin.ModelAdmin):
    list_display=('Name','Image')

admin.site.register(ContactData,AdminContactData)
admin.site.register(Application,AdminApplication)
admin.site.register(ImageUploads,AdminImageuplaods)

