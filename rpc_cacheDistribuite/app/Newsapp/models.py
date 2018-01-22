from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    date_published = models.DateField()
    category = models.CharField(max_length=100)
    num_access = models.IntegerField()
