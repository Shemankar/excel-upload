from django.db import models
from django.conf import settings

# Create your models here.
class myapp(models.Model):

    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=15)
    field3 = models.CharField(max_length=15)