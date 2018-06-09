from django.db import models


class project(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    inform = models.TextField(max_length=21845)
    middle = models.TextField(max_length=21845)
    result = models.TextField(max_length=21845)
class money(models.Model):
    quantity = models.IntegerField()
    detail = models.TextField(max_length=1000)
    proj = models.ForeignKey(project,on_delete=models.CASCADE,null=True)
class check(models.Model):
    date = models.DateField()
    log = models.TextField(max_length=21845)
    proj = models.ForeignKey(project, on_delete=models.CASCADE,null=True)
class archievement(models.Model):
    type = models.CharField(max_length=30)
    detail = models.TextField(max_length=1000)
    proj = models.ForeignKey(project, on_delete=models.CASCADE,null=True)