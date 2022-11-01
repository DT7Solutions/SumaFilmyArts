from django.db import models

# Create your models here.
class ContactData(models.Model):
            Name = models.CharField(max_length=100)
            Email = models.EmailField(max_length=254)
            Phone = models.CharField(max_length=10)
            Subject = models.CharField(max_length=100)
            Message = models.CharField(max_length=500)

            def __str__(self):
                return self.Name