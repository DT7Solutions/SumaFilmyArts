from datetime import datetime
from email.headerregistry import Address
from django.db import models
from .app import ContentTypeRestrictedFileField
from ckeditor.fields import RichTextField
# from app.extra import ContentTypeRestrictedFileField
# Create your models here.
class ContactData(models.Model):
            FirstName = models.CharField(max_length=100)
            LastName = models.CharField(max_length=100)
            Email = models.EmailField(max_length=254)
            Phone = models.CharField(max_length=10)
            Subject = models.CharField(max_length=100)
            Message = models.CharField(max_length=500)
            Date = models.DateTimeField(default=datetime.now())

            def __str__(self):
                return self.FirstName




class Application(models.Model):
    FirstName = models.CharField(max_length=50,blank=True)
    LastName = models.CharField(max_length=50,blank=True)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=10)
    Experience = models.CharField(max_length=20)
    # field_name = models.FileField(upload_to=None, max_length=254) 
    file = ContentTypeRestrictedFileField(
        upload_to='pdf',
        content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
        max_upload_size=2621440
    ) 
    # Term_check = models.BooleanField()
    Date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
                return self.FirstName


class ImageUploads(models.Model):
            Name = models.CharField(max_length=100)
            Image = models.ImageField(upload_to='uploads/')
            
            def __str__(self):
                return self.Name


class Ideas(models.Model):
            Name = models.CharField(max_length=100)
            Email = models.EmailField(max_length=254)
            Phone = models.CharField(max_length=10)
            Subject = models.CharField(max_length=400)
            file = ContentTypeRestrictedFileField(
                upload_to='pdf',
                content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
                max_upload_size=2621440
            ) 
            Date = models.DateTimeField(default=datetime.now())
            def __str__(self):
                return self.Name


class Collaboration(models.Model):
            FirstName = models.CharField(max_length=100)
            LastName = models.CharField(max_length=100)
            Email = models.EmailField(max_length=50)
            Phone = models.CharField(max_length=10)
            Brand_Agency = models.CharField(max_length=100)
            Industry = models.CharField(max_length=100)
            Collaboration_Type = models.CharField(max_length=25)
            file = ContentTypeRestrictedFileField(
                upload_to='pdf',
                content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
                max_upload_size=2621440
            ) 
            Date = models.DateTimeField(default=datetime.now())
            def __str__(self):
                return self.FirstName

class Sponsorship(models.Model):
            FirstName = models.CharField(max_length=100)
            LastName = models.CharField(max_length=100)
            Email = models.EmailField(max_length=50)
            Phone = models.CharField(max_length=10)
            Brand_Agency = models.CharField(max_length=35)
            Industry = models.CharField(max_length=30)
            Kind_Sponcer = models.CharField(max_length=30)
            Sponcer_Type = models.CharField(max_length=30)
            file = ContentTypeRestrictedFileField(
                upload_to='pdf',
                content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
                max_upload_size=2621440
            ) 
            Date = models.DateTimeField(default=datetime.now())
            def __str__(self):
                return self.FirstName
            



class Carrers(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    posted_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    Body = RichTextField(blank=True,null=True)
   

    def __str__(self):
        return self.title

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    Body = RichTextField(blank=True,null=True)
    primary_image = models.ImageField(upload_to='uploads/')
    seondary_image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    optional_image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_published = models.DateField()
    category = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    Name = models.CharField(max_length=50, default="heading")
    image = models.ImageField(upload_to='gallery-cat/',default="")
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class GalleryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery/')
    def __str__(self):
         return f"Image in Category: {self.category.Name}"
