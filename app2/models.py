from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=100, unique=True)
    post = models.CharField(max_length=20)
    salary = models.IntegerField()
    status = models.BooleanField()
    #register these to see at backend django-admin