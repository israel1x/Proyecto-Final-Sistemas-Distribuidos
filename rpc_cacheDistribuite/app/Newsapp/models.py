from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=100)
    top = models.IntegerField()


class Description(models.Model):
    news_title = models.ForeignKey(New, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
