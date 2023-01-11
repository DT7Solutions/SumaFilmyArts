from datetime import datetime
from email.headerregistry import Address
from django.db import models
from .app import ContentTypeRestrictedFileField
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
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=500)
    Experience = models.CharField(max_length=20)
    Message = models.CharField(max_length=150)
    # field_name = models.FileField(upload_to=None, max_length=254) 
    file = ContentTypeRestrictedFileField(
        upload_to='pdf',
        content_types=['application/pdf', 'application/msword','application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
        max_upload_size=2621440
    ) 
    Term_check = models.BooleanField()
    
    def __str__(self):
                return self.Name


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