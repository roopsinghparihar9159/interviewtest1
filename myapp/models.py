from django.db import models

class Employee(models.Model):
    name               = models.CharField(max_length=20)
    pannumber          = models.CharField(max_length=20, null=True)
    age                = models.CharField(max_length=3, null=True)
    gender             = models.CharField(max_length=10, null=True)
    email              = models.EmailField(max_length=120, null=True)
    city               = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.name