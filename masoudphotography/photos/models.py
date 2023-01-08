from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    cover_image = models.ImageField(upload_to ='')
    olaviat = models.DecimalField(max_digits=5, decimal_places=2)

class Photo(models.Model):
    name = models.CharField(max_length=200)
    low_quality_image = models.ImageField(upload_to ='')
    high_quality_image = models.ImageField(upload_to ='')