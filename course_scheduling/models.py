from django.db import models

# Create your models here.
class classroom(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    capacity = models.IntegerField()

class teacher(models.Model):
    name = models.CharField(max_length=30)
    #名字
    college = models.CharField(max_length=30)
    #所属学院

class lesson(models.Model):
    name = models.CharField(max_length=30)
    student_number = models.IntegerField()
    room = models.ForeignKey(classroom ,on_delete=models.SET_NULL ,null=True)
    teacher = models.ForeignKey(teacher,on_delete=models.SET_NULL,null=True)
    lesson_hour = models.IntegerField()

class time(models.Model):
    week = models.IntegerField(null=True)
    time = models.IntegerField(null=True)
    lesson = models.ForeignKey(lesson,on_delete=models.CASCADE ,null=True)
    classroom = models.ForeignKey(classroom,on_delete=models.CASCADE ,null=True)
    teacher = models.ForeignKey(teacher,on_delete=models.CASCADE ,null=True)