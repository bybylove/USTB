from django.db import models

# Create your models here.
class urlandname(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=100)